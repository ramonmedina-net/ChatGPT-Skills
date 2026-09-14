# LLM Instructions — Phased Research Continuity v1.4.0

Use this skill for research spanning multiple agents, models, sessions, usage windows, or workspaces where evidence/provenance must remain reproducible.

## Highest-priority rules

1. The declared validated artifact chain and durable files are authoritative; conversational memory is not.
2. Never silently rerun completed research.
3. Never convert progress narration into missing evidence.
4. Persist substantive state outside temporary execution storage.
5. Do not start a new bounded unit before the current unit has a durable validated checkpoint unless explicitly authorized.
6. Full validation belongs at artifact sealing; startup from a known validated checkpoint normally uses a lightweight identity/state check.
7. If durable writes fail, stop substantive work.
8. If usage/context exhaustion approaches, stop new acquisition and checkpoint.
9. Use the latest validated checkpoint as immediate predecessor.
10. Do not claim reconstructed lost material is identical without evidence.
11. Do not recursively embed predecessor checkpoints when cryptographic ancestry is sufficient.
12. Do not spend judgment-model capacity on deterministic integrity/file mechanics when a workhorse can do them.
13. A workhorse may detect ambiguity but must not resolve ambiguity outside a frozen rule.
14. Judgment decisions should be written to a structured frozen ledger; deterministic materialization should happen separately.
15. If integrity mismatches, determine byte corruption vs metadata corruption before repeating evidence acquisition.
16. Preserve historical failed integrity records; repair current metadata through an auditable reconciliation rather than rewriting history.
17. Operational checkpoints and portable releases are different artifact types; label them accurately.

## Capability routing

Classify tasks:

- J0 deterministic
- J1 extraction/structured transformation
- J2 bounded interpretation under explicit rules
- J3 substantive evidentiary judgment
- J4 methodological judgment

Default:
- J0/J1 -> workhorse
- J2 -> workhorse if closed/frozen, otherwise judgment
- J3/J4 -> judgment

Use project model-role mapping for current model names. Do not assume a particular vendor/model family will remain optimal.

## Preferred staged workflow

When appropriate:

`prepare -> plan -> acquire -> judge -> materialize -> package`

- preparation/acquisition/materialization/packaging: workhorse
- search planning and evidentiary judgment: judgment
- deterministic integrity/readiness gates: workhorse

The judgment model should consume a validated compact reading packet and should not rerun hashes, row counts, manifests, or archive checks absent a discrepancy.

## Durable handoffs

Model-role changes should be mediated by files:
- preparation handoff;
- frozen search plan;
- source/claim staging;
- readiness attestation;
- frozen adjudication decisions;
- materialization ledger;
- validated checkpoint.

## Storage

Prefer:
- one immutable canonical baseline;
- one canonical raw-evidence store;
- lightweight working trees;
- non-recursive operational checkpoints;
- flattened/deduplicated portable releases.

Operational checkpoint dependencies must be declared by project-relative path, SHA-256, and byte length.

## Block-on-ambiguity

If deterministic materialization requires substantive interpretation, do not guess. Record `BLOCKED_REQUIRES_JUDGMENT` (or project-equivalent) and return the item to the judgment tier.
