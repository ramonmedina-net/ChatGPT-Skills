#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, sys, zipfile
from pathlib import Path, PurePosixPath

EXPECTED_VERSION = "1.5.0"
EXPECTED_PREDECESSOR_VERSION = "1.4.0"
EXPECTED_RELEASE_NAME = "Git-Native Governance & Judgment-Efficient Execution"
REQUIRED_DOCTRINES = [
    "Capability-tiered execution",
    "Frozen inter-model handoffs",
    "Judgment-only adjudication and deterministic materialization",
    "Workhorse-owned readiness and integrity gates",
    "Integrity mismatch: repair before reacquisition",
    "Operational storage architecture",
    "non-recursive",
    "external dependency",
    "Git-native authority and promotion",
    "Trusted-base plus candidate validation",
    "Validator observability",
    "Self-reference-safe Git metadata",
    "Prompt provenance is append-only",
    "judgment-model budget on deterministic integrity verification",
    "accepted cumulative structured state belongs directly in Git",
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
    "templates/RUN_RECORD_TEMPLATE.json",
    "templates/PROMPT_PROVENANCE_TEMPLATE.json",
    "templates/CORRECTION_RUN_EVENT_TEMPLATE.json",
    "templates/DECISION_PACKET_TEMPLATE.json",
    "templates/GIT_MICRO_CHECKPOINT_HANDOFF_TEMPLATE.md",
    "templates/TRUSTED_BASE_CANDIDATE_VALIDATION_TEMPLATE.md",
    "templates/EVIDENCE_OBJECT_INDEX_TEMPLATE.csv",
]

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit("usage: validate_package.py PACKAGE.zip")
    zpath = Path(sys.argv[1])
    issues = []
    validation_checks = {
        "archive_integrity": "PASS",
        "path_safety": "PASS",
        "manifest_reconciliation": "PASS",
        "provenance_references": "PASS",
        "required_content": "PASS",
        "status_distribution": "PASS",
        "referential_integrity": "SKIPPED",
        "historical_loss_firewall": "SKIPPED",
    }
    validation_notes = {
        "referential_integrity": "SKIPPED: package validator has no project dataset to traverse",
        "historical_loss_firewall": "SKIPPED: package validator validates the reusable skill, not project records",
    }
    with zipfile.ZipFile(zpath) as z:
        bad = z.testzip()
        if bad:
            issues.append(f"CRC failure: {bad}")
            validation_checks["archive_integrity"] = "FAIL"
        names = z.namelist()
        if len(names) != len(set(names)):
            issues.append("duplicate ZIP member names")
            validation_checks["archive_integrity"] = "FAIL"
        path_issues = False
        for n in names:
            pp = PurePosixPath(n)
            if pp.is_absolute() or ".." in pp.parts:
                issues.append(f"unsafe path: {n}")
                path_issues = True
        if path_issues:
            validation_checks["path_safety"] = "FAIL"
        roots = {PurePosixPath(n).parts[0] for n in names if PurePosixPath(n).parts}
        if len(roots) != 1:
            issues.append(f"expected one package root, got {sorted(roots)}")
            root = ""
            validation_checks["manifest_reconciliation"] = "PREREQUISITE_MISSING"
            validation_checks["provenance_references"] = "PREREQUISITE_MISSING"
        else:
            root = next(iter(roots))
        def read(rel: str) -> bytes:
            return z.read(f"{root}/{rel}")
        manifest_readable = True
        try:
            manifest = json.loads(read("PACKAGE_MANIFEST.json"))
        except Exception as exc:
            issues.append(f"manifest unreadable: {exc}")
            manifest = {"files": []}
            manifest_readable = False
            validation_checks["manifest_reconciliation"] = "PREREQUISITE_MISSING"
            validation_checks["provenance_references"] = "PREREQUISITE_MISSING"
        if manifest.get("version") != EXPECTED_VERSION:
            issues.append("wrong manifest version")
            validation_checks["manifest_reconciliation"] = "FAIL"
        if manifest.get("predecessor_version") != EXPECTED_PREDECESSOR_VERSION:
            issues.append("wrong predecessor version")
            validation_checks["manifest_reconciliation"] = "FAIL"
        file_names = sorted(n[len(root)+1:] for n in names if n.startswith(root + "/") and not n.endswith("/"))
        expected_listed = sorted(x for x in file_names if x != "PACKAGE_MANIFEST.json")
        listed = manifest.get("files", [])
        if sorted(row.get("path","") for row in listed) != expected_listed:
            issues.append("manifest file set mismatch")
            validation_checks["manifest_reconciliation"] = "FAIL"
        reference_issues = False
        for row in listed:
            rel = row.get("path", "")
            try:
                data = read(rel)
            except KeyError:
                issues.append(f"missing manifested file: {rel}")
                reference_issues = True
                continue
            if len(data) != row.get("bytes"):
                issues.append(f"byte mismatch: {rel}")
                reference_issues = True
            if sha256(data) != row.get("sha256"):
                issues.append(f"hash mismatch: {rel}")
                reference_issues = True
        if reference_issues:
            validation_checks["provenance_references"] = "FAIL"
        elif not manifest_readable:
            validation_checks["provenance_references"] = "PREREQUISITE_MISSING"
        try:
            if read("VERSION").decode().strip() != EXPECTED_VERSION:
                issues.append("VERSION mismatch")
                validation_checks["required_content"] = "FAIL"
            skill = read("SKILL.md").decode()
            for phrase in REQUIRED_DOCTRINES:
                if phrase.lower() not in skill.lower():
                    issues.append(f"missing required doctrine: {phrase}")
                    validation_checks["required_content"] = "FAIL"
            for rel in REQUIRED_TEMPLATES:
                if rel not in file_names:
                    issues.append(f"missing required template: {rel}")
                    validation_checks["required_content"] = "FAIL"
            role_map = json.loads(read("templates/MODEL_ROLE_MAP_TEMPLATE.json"))
            if not all(k in role_map for k in ["workhorse", "judgment", "escalation_audit"]):
                issues.append("model role map missing roles")
                validation_checks["required_content"] = "FAIL"
            adj = json.loads(read("templates/ADJUDICATION_DECISION_TEMPLATE.json"))
            if not all(k in adj for k in ["decision_action", "supporting_staging_source_ids", "decision_packet_id", "judgment_model_provenance"]):
                issues.append("adjudication decision template malformed")
                validation_checks["required_content"] = "FAIL"
            recon = json.loads(read("templates/INTEGRITY_RECONCILIATION_TEMPLATE.json"))
            if not all(k in recon for k in ["classification", "historical_failed_record_preserved", "recorded_through_commit", "metadata_commit_self_excluded"]):
                issues.append("integrity reconciliation template malformed")
                validation_checks["required_content"] = "FAIL"
            readiness = json.loads(read("templates/JUDGMENT_READINESS_ATTESTATION_TEMPLATE.json"))
            if not all(k in readiness for k in ["expected_case_or_item_scope", "protected_authoritative_state_hashes", "packet_complete", "unresolved_ambiguity_flags", "allowed_judgment_scope"]):
                issues.append("judgment readiness template malformed")
                validation_checks["required_content"] = "FAIL"
            run_record = json.loads(read("templates/RUN_RECORD_TEMPLATE.json"))
            if not all(k in run_record for k in ["prompt_sha256", "custom_skill_dependencies", "recorded_through_commit", "metadata_commit_self_excluded"]):
                issues.append("run record template malformed")
                validation_checks["required_content"] = "FAIL"
            correction = json.loads(read("templates/CORRECTION_RUN_EVENT_TEMPLATE.json"))
            if not all(k in correction for k in ["correction_prompt_path", "historical_commits_rewritten", "ci_rerun_required"]):
                issues.append("correction event template malformed")
                validation_checks["required_content"] = "FAIL"
            packet = json.loads(read("templates/DECISION_PACKET_TEMPLATE.json"))
            if not all(k in packet for k in ["target_ids", "reading_index", "evidence_coverage_matrix", "allowed_judgment_scope"]):
                issues.append("decision packet template malformed")
                validation_checks["required_content"] = "FAIL"
            prompt = json.loads(read("templates/PROMPT_PROVENANCE_TEMPLATE.json"))
            if prompt.get("append_only") is not True:
                issues.append("prompt provenance template must be append-only")
                validation_checks["required_content"] = "FAIL"
            if EXPECTED_RELEASE_NAME not in read("README.md").decode():
                issues.append("README release name mismatch")
                validation_checks["required_content"] = "FAIL"
        except Exception as exc:
            issues.append(f"required-content check failed: {exc}")
            validation_checks["required_content"] = "FAIL"

    allowed_statuses = {"PASS", "FAIL", "SKIPPED", "PREREQUISITE_MISSING"}
    if not all(status in allowed_statuses for status in validation_checks.values()):
        validation_checks["status_distribution"] = "FAIL"
        issues.append("validator emitted an unrecognized validation status")
    validation_notes["status_distribution"] = "PASS: every validation section emitted an explicit status"
    result = {
        "status": "PASS" if not issues else "FAIL",
        "version": EXPECTED_VERSION,
        "archive": str(zpath),
        "archive_sha256": sha256(zpath.read_bytes()) if zpath.exists() else None,
        "issues": issues,
        "validation_checks": validation_checks,
        "validation_notes": validation_notes,
    }
    print(json.dumps(result, indent=2))
    return 0 if not issues else 1

if __name__ == "__main__":
    raise SystemExit(main())
