#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, sys, zipfile
from pathlib import Path, PurePosixPath

EXPECTED_VERSION = "1.4.0"
REQUIRED_DOCTRINES = [
    "Capability-tiered execution",
    "Frozen inter-model handoffs",
    "Judgment-only adjudication and deterministic materialization",
    "Workhorse-owned readiness and integrity gates",
    "Integrity mismatch: repair before reacquisition",
    "Operational storage architecture",
    "non-recursive",
    "external dependency",
]
REQUIRED_TEMPLATES = [
    "templates/MODEL_ROLE_MAP_TEMPLATE.json",
    "templates/EXTERNAL_DEPENDENCIES_TEMPLATE.json",
    "templates/JUDGMENT_READINESS_ATTESTATION_TEMPLATE.json",
    "templates/ADJUDICATION_DECISION_TEMPLATE.json",
    "templates/JUDGMENT_COMMIT_TEMPLATE.json",
    "templates/MATERIALIZATION_LEDGER_TEMPLATE.csv",
    "templates/INTEGRITY_RECONCILIATION_TEMPLATE.json",
    "templates/STORAGE_GROWTH_AUDIT_TEMPLATE.json",
    "templates/OPERATIONS_TELEMETRY_TEMPLATE.json",
]

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit("usage: validate_package.py PACKAGE.zip")
    zpath = Path(sys.argv[1])
    issues = []
    with zipfile.ZipFile(zpath) as z:
        bad = z.testzip()
        if bad:
            issues.append(f"CRC failure: {bad}")
        names = z.namelist()
        if len(names) != len(set(names)):
            issues.append("duplicate ZIP member names")
        for n in names:
            pp = PurePosixPath(n)
            if pp.is_absolute() or ".." in pp.parts:
                issues.append(f"unsafe path: {n}")
        roots = {PurePosixPath(n).parts[0] for n in names if PurePosixPath(n).parts}
        if len(roots) != 1:
            issues.append(f"expected one package root, got {sorted(roots)}")
            root = ""
        else:
            root = next(iter(roots))
        def read(rel: str) -> bytes:
            return z.read(f"{root}/{rel}")
        try:
            manifest = json.loads(read("PACKAGE_MANIFEST.json"))
        except Exception as exc:
            issues.append(f"manifest unreadable: {exc}")
            manifest = {"files": []}
        if manifest.get("version") != EXPECTED_VERSION:
            issues.append("wrong manifest version")
        if manifest.get("predecessor_version") != "1.3.0":
            issues.append("wrong predecessor version")
        file_names = sorted(n[len(root)+1:] for n in names if n.startswith(root + "/") and not n.endswith("/"))
        expected_listed = sorted(x for x in file_names if x != "PACKAGE_MANIFEST.json")
        listed = manifest.get("files", [])
        if sorted(row.get("path","") for row in listed) != expected_listed:
            issues.append("manifest file set mismatch")
        for row in listed:
            rel = row["path"]
            try:
                data = read(rel)
            except KeyError:
                issues.append(f"missing manifested file: {rel}")
                continue
            if len(data) != row.get("bytes"):
                issues.append(f"byte mismatch: {rel}")
            if sha256(data) != row.get("sha256"):
                issues.append(f"hash mismatch: {rel}")
        try:
            if read("VERSION").decode().strip() != EXPECTED_VERSION:
                issues.append("VERSION mismatch")
            skill = read("SKILL.md").decode()
            for phrase in REQUIRED_DOCTRINES:
                if phrase.lower() not in skill.lower():
                    issues.append(f"missing required doctrine: {phrase}")
            for rel in REQUIRED_TEMPLATES:
                if rel not in file_names:
                    issues.append(f"missing required template: {rel}")
            role_map = json.loads(read("templates/MODEL_ROLE_MAP_TEMPLATE.json"))
            if not all(k in role_map for k in ["workhorse", "judgment", "escalation_audit"]):
                issues.append("model role map missing roles")
            adj = json.loads(read("templates/ADJUDICATION_DECISION_TEMPLATE.json"))
            if "decision_action" not in adj or "supporting_staging_source_ids" not in adj:
                issues.append("adjudication decision template malformed")
            recon = json.loads(read("templates/INTEGRITY_RECONCILIATION_TEMPLATE.json"))
            if "classification" not in recon or "historical_failed_record_preserved" not in recon:
                issues.append("integrity reconciliation template malformed")
            if "Storage Architecture & Capability-Tiered Execution" not in read("README.md").decode():
                issues.append("README release name mismatch")
        except Exception as exc:
            issues.append(f"required-content check failed: {exc}")
    result = {
        "status": "PASS" if not issues else "FAIL",
        "version": EXPECTED_VERSION,
        "archive": str(zpath),
        "archive_sha256": sha256(zpath.read_bytes()) if zpath.exists() else None,
        "issues": issues,
    }
    print(json.dumps(result, indent=2))
    return 0 if not issues else 1

if __name__ == "__main__":
    raise SystemExit(main())
