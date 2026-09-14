# Phased Research Continuity Skill v1.4.0

A portable operating skill for long-running, multi-session research projects that must preserve evidence, provenance, stable identifiers, bounded search budgets, reproducibility, recoverability, and efficient model/tool use.

## Version

**1.4.0 — Storage Architecture & Capability-Tiered Execution**

This release extends v1.3.0 after a live multi-stage research batch validated three additional architectural principles:

> **Persist cumulatively without recursively duplicating immutable history.**

> **Use expensive judgment capacity for epistemic judgment, not deterministic file mechanics.**

> **When integrity disagrees, distinguish metadata corruption from evidence corruption before reacquiring evidence.**

## What v1.4.0 adds

- non-recursive operational checkpoints with cryptographic ancestry;
- external-dependency ledgers and project-relative canonical paths;
- canonical baseline/evidence-store/working/checkpoint/release storage roles;
- storage-growth and duplicate-content audits before sealing;
- runtime-debris and nested-predecessor exclusions;
- capability classes J0–J4;
- generic `workhorse`, `judgment`, and optional `escalation/audit` model roles;
- frozen inter-model handoff artifacts;
- workhorse-owned deterministic readiness/integrity gates;
- judgment-only adjudication ledgers;
- per-item durable judgment commits;
- deterministic materialization with a block-on-ambiguity rule;
- metadata-repair-before-reacquisition protocol;
- optional operations telemetry for tuning model choice and batch size.

## Core doctrine

**The agent is disposable. The model is interchangeable. Authority resides in validated artifacts, retained evidence, and explicit decision boundaries.**

A progress message, hidden scratch file, or expensive model's assertion is not a substitute for durable evidence or a validated checkpoint.

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

## Relationship to v1.3.0

v1.4.0 was built directly from the exact v1.3.0 package and preserves its continuity, recovery, micro-checkpointing, execution-status, and durable-persistence rules except where explicitly extended or superseded.

v1.3.0 predecessor SHA-256:

`abbb321e8bba67210657b5dd9a5912f875d5e4c25947c24378d0c1a910009672`

See `SKILL.md` for normative rules and `templates/` for reusable control artifacts.
