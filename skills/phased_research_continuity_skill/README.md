# Phased Research Continuity Skill v1.5.0

A portable operating skill for long-running, multi-session research projects that must preserve evidence, provenance, stable identifiers, bounded search budgets, reproducibility, recoverability, efficient model/tool use, and governed promotion of accepted state.

## Version

**1.5.0 — Git-Native Governance & Judgment-Efficient Execution**

This release extends v1.4.0 with the Git-native architecture validated during a post-migration research workflow:

> **The model is interchangeable. Authority resides in validated artifacts, governed Git history, explicit decision boundaries, and human-approved promotion.**

> **The workhorse proves the inputs are intact. The judgment tier decides what the intact inputs mean. The workhorse applies the decisions.**

## What v1.5.0 adds

- protected authoritative branch and bounded executor branches;
- pull requests as the promotion boundary, with coordinator review and human final merge;
- prompt-first, hash-backed, append-only run and correction provenance;
- durable pushed Git micro-checkpoints for bounded substantive work;
- capability-tier routing that protects judgment-model quota;
- workhorse-produced readiness attestations and compact judgment decision packets;
- reading indexes, evidence coverage matrices, and case/item-level judgment commits;
- explicit judgment/materialization separation with block-on-ambiguity behavior;
- trusted-base plus candidate validation and validator observability;
- content-addressed evidence indexes, Git LFS availability checks, and identity-only ancestry;
- self-reference-safe Git metadata using `recorded_through_commit`;
- explicit model UI/backend, custom-skill, and runtime dependency provenance.

## Core doctrine

**The agent is disposable. The durable state is not. The model is interchangeable. Authority resides in validated artifacts, retained evidence, governed Git history, and explicit decision boundaries.**

A progress message, hidden scratch file, or expensive model's assertion is not a substitute for durable evidence or a validated checkpoint.

## Governance model

The authoritative branch, normally `main`, contains accepted state only. Executors work on bounded branches, commit and push durable units, and open pull requests. The coordinator independently reviews the actual diff, commit history, CI, validation telemetry, and provenance. The human owner performs the final merge; the execution agent does not merge its own authoritative work.

For an already-authorized active unit or open pull request, the latest validated and pushed execution-branch checkpoint is the authoritative resume point for proposed work. It does not supersede accepted `main` until promotion/merge. A fresh executor resumes from that checkpoint rather than restarting from older accepted state.

Prompt provenance is preserved before substantive work. A correction prompt is a separate append-only event and produces a new commit; historical commits are not rewritten.

## Model selection

The skill intentionally does **not** hard-code current model names.

Projects map available models to roles using `templates/MODEL_ROLE_MAP_TEMPLATE.json`.

Default routing:

- **J0–J1:** workhorse
- **J2:** workhorse when the rule is explicit/closed; otherwise judgment
- **J3–J4:** judgment
- unusual disagreement or adversarial review: optional escalation/audit role

This keeps the skill valid as model families, pricing, and quotas change.

## Storage selection

Operational checkpoints may reference canonical assets elsewhere in the durable project tree through an explicit dependency ledger.

Portable releases remain self-contained (or explicitly paired with a canonical evidence bundle) and should flatten/deduplicate rather than recursively embed predecessor archives.

For Git-native projects where repository policy, data classification/sensitivity, storage size, and technical constraints permit it, current accepted cumulative structured state lives directly in Git. Immutable evidence should be content-addressed or hash-indexed, and large/binary objects may use Git LFS when configured and available. Operational checkpoints identify ancestry and dependencies cryptographically without recursive archive copies.

Where authoritative structured data cannot appropriately live in Git, use an external authoritative structured store while keeping schemas, manifests, indexes, immutable snapshot identities, hashes/version IDs, durable locators, and validated dependency records in Git. This preserves the governance boundary without making direct Git storage mandatory for every research program.

## Checkpoint choices

- **Git-native operational checkpoint:** a validated pushed execution-branch commit plus sufficient run state, provenance, handoff, and validator evidence. It does not require a ZIP at every case, stage, or micro-batch.
- **Artifact-native operational checkpoint:** the existing immutable checkpoint/archive workflow for non-Git projects or projects that explicitly require sealed artifacts.
- **Portable release / sealing milestone:** explicit packaging and independent archive validation when portability, migration, release sealing, or project policy requires it.

To build this skill package deterministically across Windows and Linux, run:

```text
python skills/phased_research_continuity_skill/build_package.py --output <package.zip>
python skills/phased_research_continuity_skill/validate_package.py <package.zip>
```

The builder normalizes intended text members to LF, uses deterministic ordering and ZIP metadata, excludes runtime debris, and verifies all non-manifest members against `PACKAGE_MANIFEST.json`.

## Compatibility with v1.4.0

v1.5.0 preserves v1.4.0's continuity, recovery, bounded execution, storage architecture, capability classes, readiness gates, judgment ledgers, deterministic materialization, integrity reconciliation, and operational-versus-portable release distinction. It intentionally supersedes informal branch/provenance assumptions with Git-native authority, prompt-first run records, trusted-base validation, explicit observability, and human-controlled PR promotion.

See `SKILL.md` for normative rules and `templates/` for reusable control artifacts.
