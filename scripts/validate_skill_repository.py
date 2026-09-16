#!/usr/bin/env python3
"""Repository-level structural validator for ChatGPT-Skills.

This validator is intentionally version-agnostic. It validates candidate
repository state independently of each skill's own validator so a pull request
cannot evade the trusted baseline merely by weakening its candidate validator.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path


TEXT_SUFFIXES = {
    ".csv", ".json", ".md", ".ps1", ".py",
    ".txt", ".toml", ".yaml", ".yml",
}
TEXT_FILENAMES = {"VERSION"}
SKIP_DIRS = {".git", "__pycache__"}
SKIP_SUFFIXES = {".pyc", ".pyo"}


def canonical_bytes(path: Path) -> bytes:
    data = path.read_bytes()
    if path.name in TEXT_FILENAMES or path.suffix.lower() in TEXT_SUFFIXES:
        data = data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return data


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fail(category: str, message: str, issues: list[tuple[str, str]]) -> None:
    issues.append((category, message))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    args = parser.parse_args()

    root = args.root.resolve()
    skills_root = root / "skills"
    issues: list[tuple[str, str]] = []

    if not skills_root.is_dir():
        print("repo_structure=FAIL")
        print("ERROR: skills/ directory missing")
        return 1

    skill_dirs = sorted(
        path
        for path in skills_root.iterdir()
        if path.is_dir() and (path / "PACKAGE_MANIFEST.json").is_file()
    )

    if not skill_dirs:
        print("repo_structure=FAIL")
        print("ERROR: no manifested skills found")
        return 1

    for skill in skill_dirs:
        manifest_path = skill / "PACKAGE_MANIFEST.json"

        try:
            manifest = json.loads(canonical_bytes(manifest_path))
        except Exception as exc:
            fail(
                "manifest_reconciliation",
                f"{skill.name}: unreadable PACKAGE_MANIFEST.json: {exc}",
                issues,
            )
            continue

        for required in ("SKILL.md", "README.md"):
            if not (skill / required).is_file():
                fail(
                    "repo_structure",
                    f"{skill.name}: missing required file {required}",
                    issues,
                )

        version_path = skill / "VERSION"
        if version_path.is_file():
            version = canonical_bytes(version_path).decode("utf-8").strip()
            if manifest.get("version") != version:
                fail(
                    "version_consistency",
                    f"{skill.name}: VERSION={version!r} "
                    f"but manifest version={manifest.get('version')!r}",
                    issues,
                )

        rows = manifest.get("files")
        if not isinstance(rows, list):
            fail(
                "manifest_reconciliation",
                f"{skill.name}: manifest files field is not a list",
                issues,
            )
            continue

        listed_paths = [row.get("path", "") for row in rows]

        if len(listed_paths) != len(set(listed_paths)):
            fail(
                "manifest_reconciliation",
                f"{skill.name}: duplicate manifest paths",
                issues,
            )

        if "PACKAGE_MANIFEST.json" in listed_paths:
            fail(
                "manifest_reconciliation",
                f"{skill.name}: manifest must not hash itself",
                issues,
            )

        actual_paths: list[str] = []

        for path in sorted(skill.rglob("*")):
            if not path.is_file():
                continue

            rel = path.relative_to(skill)

            if any(part in SKIP_DIRS for part in rel.parts):
                continue

            if path.suffix.lower() in SKIP_SUFFIXES:
                fail(
                    "runtime_debris",
                    f"{skill.name}: runtime debris committed: {rel.as_posix()}",
                    issues,
                )
                continue

            rel_name = rel.as_posix()

            if rel_name == "PACKAGE_MANIFEST.json":
                continue

            actual_paths.append(rel_name)

        if sorted(actual_paths) != sorted(listed_paths):
            missing = sorted(set(listed_paths) - set(actual_paths))
            extra = sorted(set(actual_paths) - set(listed_paths))
            fail(
                "manifest_reconciliation",
                f"{skill.name}: file-set mismatch; "
                f"missing={missing}; extra={extra}",
                issues,
            )

        for row in rows:
            rel = row.get("path", "")
            path = skill / rel

            if not path.is_file():
                continue

            data = canonical_bytes(path)

            if row.get("bytes") != len(data):
                fail(
                    "canonical_hashes",
                    f"{skill.name}/{rel}: byte-count mismatch",
                    issues,
                )

            if row.get("sha256") != sha256(data):
                fail(
                    "canonical_hashes",
                    f"{skill.name}/{rel}: SHA-256 mismatch",
                    issues,
                )

        for json_path in skill.rglob("*.json"):
            rel = json_path.relative_to(skill)

            if any(part in SKIP_DIRS for part in rel.parts):
                continue

            try:
                json.loads(canonical_bytes(json_path))
            except Exception as exc:
                fail(
                    "json_parse",
                    f"{skill.name}/{rel.as_posix()}: invalid JSON: {exc}",
                    issues,
                )

    categories = {
        "repo_structure",
        "manifest_reconciliation",
        "version_consistency",
        "canonical_hashes",
        "json_parse",
        "runtime_debris",
    }

    failed_categories = {category for category, _ in issues}

    print(f"skills_discovered={len(skill_dirs)}")

    for category in sorted(categories):
        print(
            f"{category}="
            f"{'FAIL' if category in failed_categories else 'PASS'}"
        )

    if issues:
        print("\nValidation issues:")
        for category, message in issues:
            print(f"- [{category}] {message}")
        return 1

    print("repository_validation=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
