# LLM Instructions — Phased Research Continuity v1.5.0

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
18. The authoritative branch is protected accepted state; execution branches are proposed state until promotion through a reviewed pull request.
19. The executor may commit, push, and open a pull request but must not write to protected `main`, force-push, delete governed branches, or merge its own authoritative work.
20. The coordinator reviews the actual Git diff, commits, CI, validator output, and provenance—not merely the executor's narrative. Human ownership performs the final merge.
21. Preserve and hash the exact invocation prompt before substantive work; commit and push the provenance first. Correction prompts are separate append-only events.
22. Do not spend judgment-model budget on deterministic integrity verification. The workhorse handles J0/J1 continuity work and constructs the validated decision packet.
23. A lower-authority model may detect ambiguity but must not silently resolve it outside frozen rules. Escalate and preserve the evidence.
24. A pushed commit is a durable external checkpoint; a local commit or chat update is not.
25. Validate the trusted-base validator as well as the candidate validator when practical, and emit telemetry for executed, failed, skipped, and prerequisite-missing checks.
26. Never store the SHA of a metadata-bearing commit inside that same metadata record; use `recorded_through_commit` and `metadata_commit_self_excluded`.
27. The protected authoritative branch is accepted state. For an already-authorized active unit or open pull request, the latest validated and pushed execution-branch checkpoint is the authoritative resume point for proposed work; it does not supersede accepted state until promotion/merge.
28. Select a checkpoint form per project: a Git-native operational checkpoint is a validated pushed commit plus sufficient evidence and does not require a ZIP at every micro-batch; an artifact-native checkpoint retains immutable archive validation; a portable release still requires explicit sealing and independent archive validation.
29. Use the supported deterministic package builder for this skill: `python skills/phased_research_continuity_skill/build_package.py --output <package.zip>`, then run `validate_package.py` against the produced ZIP.

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

`prepare -> plan -> acquire -> judge -> materialize -> checkpoint -> package_if_required`

- preparation/acquisition/materialization/packaging: workhorse
- search planning and evidentiary judgment: judgment
- deterministic integrity/readiness gates: workhorse

The judgment model should consume a validated compact reading packet and should not rerun hashes, row counts, manifests, or archive checks absent a discrepancy.

The readiness attestation should identify expected scope, frozen acquisition state, evidence and capture integrity, target counts, protected-state hashes, packet completeness, unresolved ambiguity flags, allowed judgment scope, and clarification reserve. The judgment tier verifies the attestation and packet identity instead of rediscovering the workspace.

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

For Git-native projects where policy, sensitivity, storage size, and technical constraints permit it, current accepted cumulative structured state lives directly in Git. Historical accepted states come from Git history and tags rather than recursive version directories. If authoritative structured data cannot appropriately live in Git, use an external authoritative store with Git-tracked schemas/manifests/indexes, immutable snapshot identity, hashes/version IDs, durable locators, and validated dependency records. Immutable evidence should be content-addressed or hash-indexed; Git LFS may hold large/binary artifacts, but a pointer alone does not prove availability.

Record model UI label, backend identifier or `unavailable`, role, and configuration. Record custom-skill dependencies separately from runtime dependencies; use an empty custom-skill list when none was invoked.

When resuming after interruption, reconcile the latest pushed execution-branch checkpoint for the active proposed unit before consulting older accepted state. Do not confuse proposed resume authority with accepted authority.

## Deterministic package build

The supported builder normalizes intended text members to LF, uses deterministic ordering and ZIP metadata, excludes runtime debris, and verifies all non-manifest members against `PACKAGE_MANIFEST.json`. The manifest remains excluded from its own hash list. A Git-native checkpoint does not require invoking the builder unless a package or sealing milestone is required.

## Block-on-ambiguity

If deterministic materialization requires substantive interpretation, do not guess. Record `BLOCKED_REQUIRES_JUDGMENT` (or project-equivalent) and return the item to the judgment tier.

## Git-native promotion

Use the flow:

`executor branch -> pull request -> coordinator review -> human final merge`

Do not merge the pull request as the execution agent. If review finds a defect, preserve a separate correction prompt/event, add a new commit, rerun CI, and re-review. Do not rewrite historical commits or re-adjudicate conclusions during an infrastructure-only correction.
