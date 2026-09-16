# Changelog

## 1.5.0 — 2026-09-15
### Added
- Git-native authority model separating protected accepted state, executor branches, pull-request promotion, coordinator review, and human final merge.
- Prompt-first provenance with exact prompt preservation, SHA-256 identity, append-only run records, and separate correction events.
- Durable pushed Git micro-checkpoints and interruption-resilient case/item-level judgment commits.
- Judgment-efficient capability routing: deterministic J0/J1 work stays with the workhorse, while J3/J4 judgment is reserved for epistemically substantive decisions.
- Workhorse-produced judgment-readiness attestations, compact decision packets, reading indexes, and evidence coverage matrices.
- Trusted-base plus candidate validation doctrine and explicit validator observability statuses.
- Content-addressed evidence-object index, Git LFS availability metadata, self-reference-safe Git fields, and explicit model/skill/runtime provenance.
- Run, prompt, correction, decision-packet, Git handoff, trusted-validation, and evidence-index templates.
- Deterministic cross-platform `build_package.py` for canonical LF package bytes, stable ordering, fixed ZIP metadata, runtime-debris exclusion, and manifest reconciliation.

### Changed
- The protected authoritative branch remains accepted state, while the latest validated pushed checkpoint on an authorized active execution branch is the resume authority for proposed work until promotion.
- Git-native operational checkpoints no longer require ZIP packaging at every bounded unit; artifact-native checkpoints and explicit portable sealing milestones retain independent archive validation.
- Git storage of accepted structured state is recommended only where repository policy, sensitivity, storage size, and technical constraints permit it; otherwise an external authoritative store may be paired with Git-tracked identities and dependency records.
- The authoritative current structured state for Git-native projects is stored directly in Git; historical accepted states are recovered through history and tags rather than recursive cumulative copies.
- A lower-authority model may flag ambiguity but may not silently resolve it outside frozen rules.
- The judgment tier consumes validated packets and does not repeat deterministic integrity work unless an attestation is suspect.
- Infrastructure corrections are new commits with CI reruns and re-review; historical commits are not rewritten and research conclusions are not re-adjudicated without explicit authorization.

### Preserved
- v1.4.0 continuity, recovery, storage, capability-tier, readiness, adjudication, materialization, integrity-reconciliation, and operational-versus-portable-release behavior.

## 1.4.0 — 2026-09-14
### Added
- Non-recursive operational-checkpoint architecture.
- Cryptographic ancestry and external dependency ledgers.
- Canonical baseline/evidence-store/working/checkpoint/release storage roles.
- Storage-growth, duplicate-content, and nested-archive audits.
- Explicit runtime-debris exclusion rules.
- J0–J4 capability classification.
- Generic workhorse, judgment, and escalation/audit model roles.
- Project-level model-role mapping template.
- Frozen inter-model handoff doctrine.
- Workhorse-owned deterministic readiness/integrity gates.
- Judgment-only adjudication decision ledgers.
- Per-item durable judgment commits.
- Deterministic materialization ledger with block-on-ambiguity behavior.
- Metadata-repair-before-reacquisition protocol.
- Integrity reconciliation template.
- External-dependency template.
- Judgment readiness attestation template.
- Operations telemetry template.

### Changed
- Operational checkpoints may rely on declared canonical external dependencies; portable releases remain distinct and self-contained.
- Predecessor history is preserved by cryptographic lineage rather than recursively embedding predecessor ZIPs.
- Judgment-model capacity is treated as a protected resource and should not be spent on hashing, schema checks, packaging, or bulk row materialization.
- Expensive adjudication should persist item/case decisions incrementally so quota interruption does not force repeated judgment.
- Integrity mismatches no longer imply automatic research repetition; metadata-only defects may be repaired with immutable audit provenance.

## 1.3.0 — 2026-09-10
### Added
- Durable Execution Protocol.
- Persistence proof test for new storage.
- Micro-batch execution units and cumulative checkpoint chaining.
- Coordinator/executor separation.
- Tiered validation: lightweight startup vs full artifact sealing.
- Emergency checkpoint protocol.
- Material-loss historical-progress firewall.
- Explicit reconstruction rules for lost deterministic selections.
- Separate authorization/new-ID requirement for replacement research.
- Checkpoint receipts and durable coordinator state.
- Immediate-predecessor semantics for cumulative batch chains.
- Explicit rule that durable-write failure stops substantive research.

### Changed
- Refined session rollover from “fresh chat per phase” to “fresh execution context per bounded unit when advantageous.”
- Clarified that hidden workspace state and progress messages are not durable evidence.
- Clarified that unused budget does not automatically carry forward.
- Clarified that full validation should not be repeated at every startup absent discrepancy.

## 1.2.0
Documented behavior carried forward:
- usage/quota interruption recovery;
- execution-status tracking;
- reconcile surviving state before continuing;
- do not repeat completed searches;
- preserve capture-loss states and separately log recoveries;
- reconstruct only missing derived/release files.

## 1.1.0
Documented behavior carried forward:
- session/conversation rollover;
- fresh conversation may resume from file state;
- file continuity mandatory, transcript continuity optional.

## 1.0.0
Initial documented Phased Research Continuity workflow:
- immutable predecessor;
- manifest/hash/count/schema validation;
- stable IDs and provenance;
- bounded phases;
- contemporaneous search logging;
- machine-derived summaries;
- immutable successor bundle;
- independent reopen/verification.
