#!/usr/bin/env python3
"""Build a deterministic, cross-platform ZIP for this skill package.

The manifest describes canonical LF bytes. This builder normalizes intended
text members before validating them against PACKAGE_MANIFEST.json, so a
Windows checkout with core.autocrlf enabled has the same package semantics as
a Linux checkout.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import zipfile
from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parent
PACKAGE_NAME = PACKAGE_ROOT.name
TEXT_SUFFIXES = {".csv", ".json", ".md", ".py", ".txt", ".toml", ".yaml", ".yml"}
TEXT_FILENAMES = {"VERSION"}
SKIP_DIRS = {"__pycache__", ".git"}
SKIP_SUFFIXES = {".pyc", ".pyo", ".zip"}
FIXED_ZIP_TIMESTAMP = (1980, 1, 1, 0, 0, 0)


def canonical_bytes(path: Path) -> bytes:
    data = path.read_bytes()
    if path.name in TEXT_FILENAMES or path.suffix.lower() in TEXT_SUFFIXES:
        data = data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return data


def iter_members() -> list[tuple[str, bytes]]:
    members: list[tuple[str, bytes]] = []
    for path in sorted(PACKAGE_ROOT.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(PACKAGE_ROOT)
        if any(part in SKIP_DIRS for part in relative.parts):
            continue
        if path.suffix.lower() in SKIP_SUFFIXES:
            continue
        members.append((relative.as_posix(), canonical_bytes(path)))
    return members


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def validate_manifest(members: list[tuple[str, bytes]]) -> dict:
    manifest_path = PACKAGE_ROOT / "PACKAGE_MANIFEST.json"
    try:
        manifest = json.loads(canonical_bytes(manifest_path))
    except Exception as exc:  # pragma: no cover - command-line error path
        raise SystemExit(f"cannot read PACKAGE_MANIFEST.json: {exc}") from exc

    actual = {path: data for path, data in members if path != "PACKAGE_MANIFEST.json"}
    listed = {row.get("path", ""): row for row in manifest.get("files", [])}
    if "PACKAGE_MANIFEST.json" in listed:
        raise SystemExit("PACKAGE_MANIFEST.json must remain excluded from its own file list")
    if sorted(actual) != sorted(listed):
        missing = sorted(set(listed) - set(actual))
        extra = sorted(set(actual) - set(listed))
        raise SystemExit(f"manifest file set mismatch; missing={missing}; extra={extra}")
    for path, data in actual.items():
        row = listed[path]
        if row.get("bytes") != len(data) or row.get("sha256") != sha256(data):
            raise SystemExit(f"manifest hash/byte mismatch for {path}")
    return manifest


def write_package(output: Path, members: list[tuple[str, bytes]]) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_STORED) as archive:
        for relative, data in members:
            info = zipfile.ZipInfo(f"{PACKAGE_NAME}/{relative}", FIXED_ZIP_TIMESTAMP)
            info.create_system = 3
            info.create_version = 20
            info.extract_version = 20
            info.flag_bits = 0x800
            info.compress_type = zipfile.ZIP_STORED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=PACKAGE_ROOT.parents[1] / "dist" / f"{PACKAGE_NAME}.zip",
        help="output ZIP path (default: repository dist directory)",
    )
    args = parser.parse_args()

    members = iter_members()
    manifest = validate_manifest(members)
    write_package(args.output, members)
    print(
        json.dumps(
            {
                "status": "PASS",
                "package": str(args.output.resolve()),
                "version": manifest.get("version"),
                "members": len(members),
                "canonical_text_encoding": "LF",
                "zip_compression": "stored",
                "zip_timestamp": "1980-01-01T00:00:00Z",
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
