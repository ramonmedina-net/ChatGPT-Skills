# Skill: Phased Research Continuity
Version: 1.5.0
Release: Git-Native Governance & Judgment-Efficient Execution

## Purpose

Use this skill for complex research programs that:
- span multiple conversations, agents, models, usage windows, or context windows;
- use structured datasets, source registries, search logs, candidate ledgers, or coding tables;
- require reproducible bounded research;
- must survive interruptions without repeating completed work;
- produce versioned checkpoints or releases.

The skill governs **continuity, persistence, provenance, validation, and recovery**. It does not replace a project's substantive research protocol.

The agent is disposable. The durable state is not. The model is interchangeable. Authority resides in validated artifacts, governed Git history, explicit decision boundaries, and human-approved promotion.

The operational routing principle is:

> The workhorse proves the inputs are intact. The judgment tier decides what the intact inputs mean. The workhorse applies the decisions.

---

## 1. Authority hierarchy

Use this hierarchy unless the project explicitly defines a stricter one:

1. latest accepted state on the protected authoritative branch, normally represented by a reviewed pull-request merge;
2. latest independently validated immutable release/checkpoint;
3. durable incremental working files descended from that artifact;
4. retained raw evidence/captures and contemporaneous logs;
5. machine-derived summaries reproduced from those files;
6. progress reports/messages;
7. conversational memory.

Lower layers may explain higher layers but may not overwrite them without source-backed controlled change.

A valid commit on an execution branch is proposed state, not accepted state, until it crosses the pull-request promotion boundary and is merged according to repository governance.

**Conversation memory is never a substitute for missing evidence.**

---

## 2. Immutable predecessor rule

At the start of a new phase or execution unit:

- identify exactly one authoritative predecessor artifact;
- preserve it unchanged;
- record its filename/version and SHA-256;
- never mutate the predecessor in place;
- write changes to a new working tree and later to a successor checkpoint/release.

When a sequence contains micro-batches, the immediate predecessor is the **latest validated cumulative checkpoint**, not the original phase baseline.

Example:

`v09 -> infrastructure checkpoint -> B01 -> B02 -> B03 -> final v10`

B03 inherits cumulative state from B02, while the original baseline remains preserved for ancestry/audit.

---

## 3. Validation levels

### 3.1 Full validation — artifact creation/sealing

Perform full independent validation when:
- creating a new immutable checkpoint;
- creating a release;
- repairing a detected integrity discrepancy;
- conducting an explicit audit;
- the predecessor has not previously been validated.

As applicable, check:
- ZIP/archive CRC;
- safe and unique paths;
- manifest completeness;
- SHA-256 and byte counts;
- CSV row counts and schemas;
- stable-ID uniqueness;
- referential integrity;
- search-budget accounting;
- capture accounting;
- source/provenance linkage;
- controlled-change linkage;
- machine-summary reproduction;
- project-specific completion requirements.

Independently reopen the packaged artifact. Do not validate only the source directory that was packaged.

### 3.2 Lightweight startup validation — consumption of a known checkpoint

When starting from an already independently validated immutable checkpoint, normally verify only:
- checkpoint identity/hash;
- expected predecessor/version;
- expected high-level counts/state;
- required next-unit assignment;
- absence/presence of expected log rows;
- durable storage writability.

Do **not** rerun expensive historical validators merely as ritual.

Escalate to full validation if any startup value disagrees.

---

## 4. Durable execution protocol

For substantive work, establish a durable working location before expensive research begins.

Preferred architecture:

`validated predecessor -> durable working tree -> immutable checkpoint -> next execution unit`

The active agent/workspace is disposable; the filesystem/artifact chain carries state.

### 4.1 Persistence test

For a new storage mechanism:
1. write a small file containing timestamp + random nonce;
2. calculate SHA-256;
3. reopen it from disk/storage and verify hash;
4. in a fresh agent/session, read it again and reproduce the hash when practical.

Do not assume a location is durable merely because an agent says it wrote a file.

### 4.2 Incremental flush requirement

Persist state as substantive operations complete.

After a search:
- append/prelog search row;
- record execution/capture status;
- save raw capture/retrieval evidence where feasible;
- register new source metadata.

After adjudication:
- persist decision;
- persist source independence assessment where relevant;
- persist fact-level provenance or coding.

After a completed case/item:
- persist all affected tables;
- update execution status;
- record durable completion time.

Do not wait until the end of a long phase to persist everything.

### 4.3 Write failure

If the designated durable store becomes unavailable or unwritable:
- stop new substantive research;
- preserve whatever is safely recoverable;
- report the failure;
- do not continue accumulating evidence solely in temporary storage.

---

## 5. Bounded execution units and micro-checkpoints

A research phase may be divided into multiple bounded execution units.

Each unit should define before substantive work:
- unit/batch ID;
- exact scope or selected items;
- search/tool budget if applicable;
- search-ID namespace;
- completion criteria;
- checkpoint destination;
- prohibited adjacent work.

A unit should be small enough that:
- state can be persisted frequently;
- a failure has bounded cost;
- validation/packaging is feasible within the usage window.

Do not optimize batch size upward after only one successful run. Use observed workload and failure history.

### Unit lifecycle

1. lightweight predecessor identity check;
2. initialize durable working directory;
3. record execution status;
4. review inherited evidence first;
5. conduct only authorized substantive work;
6. persist incrementally;
7. derive summaries programmatically;
8. package immutable cumulative checkpoint;
9. independently validate checkpoint;
10. update coordinator state / receipt;
11. stop and await authorization for next unit.

Unused search capacity does not automatically carry forward unless the protocol explicitly says it does.

---

## 6. Coordinator/executor separation

For complex programs, separate roles where useful.

### Coordinator
Responsible for:
- selecting the authoritative checkpoint;
- approving bounded units;
- reviewing returned checkpoints;
- deciding next scope/budget;
- maintaining methodological continuity;
- avoiding scope drift.

The coordinator need not perform substantive research.

### Execution agent
Responsible for:
- working only within the authorized unit;
- using durable local/cloud storage;
- logging and preserving evidence;
- producing the validated successor checkpoint;
- stopping after the assigned unit.

For Git-native projects, the execution agent works on a bounded execution branch, commits durable progress, pushes those commits, and may open a pull request. It must not write directly to the protected authoritative branch, force-push, delete governed branches, or merge its own authoritative work.

The coordinator should inspect what actually landed in Git: the branch, commits, diff, CI results, validation logs, and provenance artifacts. A final narrative is not a substitute for independent inspection.

The preferred promotion path is:

`executor branch -> pull request -> coordinator review -> human final merge`

The coordinator may approve or request changes but should not normally perform the final merge. Any exception must be an explicit project governance override.

A coordinator conversation may be replaced. A Work/execution thread may be replaced. Neither replacement should threaten the research if the durable artifact chain is complete.

---

## 7. Search and acquisition accounting

For projects with bounded discovery/verification:

- assign unique search IDs;
- preserve exact literal queries;
- prelog or contemporaneously log each query;
- count each submitted query according to the project's budget rule;
- do not hide multiple searches in batching;
- preserve execution state separately from capture state;
- recovery searches receive new IDs;
- never overwrite a lost search with its recovery.

Recommended states:
- `planned`
- `not_executed`
- `executed_capture_retained`
- `executed_capture_lost`
- `recovery_repeat_executed`

If a known page/document is opened without a new search query, log it as retrieval/evidence acquisition when the project requires provenance, but do not misclassify it as a search.

---

## 8. Existing-evidence-first rule

Before new searching for an item/case:
- inspect inherited records;
- inspect linked sources/captures;
- inspect notes/candidate decisions;
- identify exact material gaps;
- search only for unresolved facts, conflicts, weak support, or required enrichment.

Do not rediscover facts merely because a fresh agent has not personally seen them before.

---

## 9. Usage/quota/context interruption recovery

When execution stops unexpectedly:

### First action
Inventory and reconcile. Do not search first.

Inspect:
- immutable predecessor;
- durable working tree;
- execution-status file;
- search log;
- raw captures;
- candidate/adjudication ledgers;
- source/source-link tables;
- fact provenance;
- controlled changes;
- partial successor tables;
- summaries;
- manifests;
- checkpoint/release artifacts.

Compare:
- row counts;
- last IDs;
- timestamps;
- hashes where useful;
- planned vs executed search states;
- completed vs partial items.

Then continue **only unfinished work**.

If search acquisition is complete:
> resume with adjudication, summary, integrity, and packaging—not research repetition.

If substantive work is complete:
> resume with packaging/validation only.

---

## 10. Emergency checkpoint protocol

If usage, context length, tool availability, or workspace stability appears likely to end before the unit completes:

1. stop initiating new searches/acquisition;
2. flush logs/captures/adjudication;
3. record completed and partial items;
4. record remaining budget;
5. record last IDs;
6. package a partial checkpoint if feasible;
7. independently validate what was packaged;
8. stop.

Do not spend the final available execution time squeezing in extra research while leaving completed evidence unsealed.

A partial checkpoint must never masquerade as a completed release.

---

## 11. Material-loss protocol

If substantive working files are absent after interruption:

### 11.1 Establish the loss
Search reasonable known durable/scratch locations once. Do not burn large research budgets repeatedly searching for files without a specific new lead.

### 11.2 Preserve the intact predecessor
The latest intact validated predecessor remains authoritative.

### 11.3 Create a loss inventory
Record:
- what is intact;
- what is missing;
- last reported progress;
- whether raw evidence survived;
- whether IDs/logs survived;
- whether any successor artifact survived.

### 11.4 Historical-progress firewall
Progress messages such as “64/90 searches complete” are **loss provenance only** unless their underlying records/captures survive.

Do not recreate:
- search IDs;
- literal queries;
- raw captures;
- source rows;
- fact assertions;
- adjudication outcomes;
- controlled changes

from a progress message alone.

Use a separate historical-loss ledger with a status such as:

`unverified_historical_report_only`

Do not insert those reports into authoritative search logs.

### 11.5 Recovery checkpoint
Package the intact predecessor plus:
- loss inventory;
- handoff;
- relevant assignment/protocol;
- validation metadata.

Label it clearly as incomplete. Never call it a completed successor release.

---

## 12. Reconstruction after material loss

Reconstruction is permitted only from surviving authoritative inputs and deterministic specifications.

Examples of safely reconstructible material:
- empty schemas;
- deterministic queues;
- derived tables reproducible from predecessor data;
- deterministic scoring outputs;
- blank execution-status scaffolds.

Examples of material that is **not** reconstructible without evidence:
- lost raw captures;
- lost search result contents;
- lost source adjudication;
- lost fact-level provenance;
- lost controlled corrections based on unavailable evidence.

### 12.1 Lost deterministic selection

If a selection file is lost:
- reproduce it only if the complete original algorithm/specification is recoverable;
- compare hashes/IDs if possible;
- otherwise create a new deterministic reconstruction selection;
- document the limitation;
- never claim identity with the lost selection without evidence.

### 12.2 Replacement research

Replacement research must:
- be separately authorized;
- use new IDs/namespaces;
- use a newly declared budget;
- preserve the historical-loss record;
- never masquerade as the lost original execution.

---

## 13. Source and fact provenance

Research datasets should distinguish:
- source record;
- source-to-entity link;
- independent evidentiary origin;
- fact assertion;
- support/contradiction relation;
- attribution type;
- controlled change.

Multiple URLs do not necessarily equal independent evidence.

When reliable sources conflict:
- preserve competing assertions;
- record each source;
- record the resolution rationale if one is chosen;
- otherwise preserve explicit conflict/unknown status.

Never silently convert `unknown`, `not_researched`, `not_found`, or conflicting evidence into `no`.

---

## 14. Controlled change

Never silently overwrite an inherited research fact.

For each authoritative change, record where applicable:
- change ID;
- entity/item ID;
- field;
- old value;
- new value;
- change type;
- rationale;
- source IDs;
- phase/unit;
- timestamp.

Distinguish:
- factual correction;
- precision improvement;
- normalization;
- conflict resolution;
- duplicate disposition;
- controlled addition.

Do not call every changed cell an “error.”

---

## 15. Stable IDs, cryptographic ancestry, and non-recursive storage

- preserve inherited stable IDs;
- never renumber to make tables tidy;
- if duplicate records merge, retain historical IDs/aliases;
- new IDs must use collision-resistant namespaces;
- every successor must make its ancestry explicit.

Record at minimum:
- immediate predecessor ID/version;
- canonical predecessor path or artifact locator;
- predecessor SHA-256;
- predecessor byte length;
- earlier baseline identity;
- reconstruction/migration ancestors where relevant;
- unit/batch lineage.

### 15.1 Do not recursively embed predecessor checkpoints

Operational checkpoints should identify predecessor artifacts **cryptographically**, not by nesting entire predecessor archives.

Preferred lineage:

`baseline -> checkpoint A -> checkpoint B -> checkpoint C`

represented by IDs, hashes, lengths, manifests, and dependency ledgers.

Avoid:

`checkpoint C.zip -> checkpoint B.zip -> checkpoint A.zip`

unless a project explicitly requires a portable nested archive and accepts the storage cost.

### 15.2 Canonical immutable assets

Maintain one canonical copy of large immutable assets where practical:
- baselines;
- predecessor checkpoints;
- raw evidence objects;
- large source documents.

Working batches and operational checkpoints should reference those assets by durable project-relative path + SHA-256 + byte length rather than silently duplicating bytes.

A portable release may flatten required dependencies into one self-contained package, but should deduplicate identical content rather than recursively embedding old releases.

### 15.3 Content-addressed or hash-indexed evidence

Prefer a canonical evidence store in which each retained byte object is stored once and indexed by SHA-256.

If a content-addressed store is not practical, maintain an evidence index containing at least:
- capture/object ID;
- SHA-256;
- byte length;
- canonical path;
- source/search/case linkage;
- MIME/type metadata;
- acquisition batch.

Multiple logical references may point to the same canonical byte object.

---

## 16. Execution-status file

Maintain a machine-readable execution-status file during long units.

Recommended fields:
- project;
- phase;
- unit/batch ID;
- authoritative predecessor;
- predecessor SHA-256;
- authorized scope;
- authorized search budget;
- planned/executed searches;
- capture losses/recoveries;
- items started/completed;
- last completed item;
- last search ID;
- raw capture count;
- sources added;
- provenance rows;
- controlled changes;
- current state;
- last durable update;
- checkpoint status;
- release status.

Update it frequently enough that a fresh session can determine exactly where to resume.

See `templates/EXECUTION_STATUS_TEMPLATE.json`.

---

## 17. Operational checkpoint vs portable release

### Operational checkpoint
A durable continuation artifact optimized for resuming work inside a known persistent project environment.

It may represent:
- a completed micro-batch;
- a partial interrupted batch;
- infrastructure reconstruction;
- recovery after loss.

An operational checkpoint may depend on canonical immutable assets stored elsewhere in the durable project root, but every dependency must be declared by:
- dependency ID;
- role;
- project-relative canonical path;
- SHA-256;
- byte length;
- required/optional status;
- validation state.

Its manifest must say that it is an operational checkpoint and **not** a portable release.

### Portable release
A phase-level or milestone-level artifact intended to remain usable after separation from the original project filesystem.

A portable release should:
- contain all required cumulative structured state;
- include required evidence bytes or a separately delivered canonical evidence bundle;
- flatten/deduplicate content rather than embedding recursive predecessor ZIPs;
- pass independent validation after packaging.

Never call an infrastructure checkpoint, recovery checkpoint, partial batch, or externally dependent operational checkpoint a portable completed release.

---

## 18. Checkpoint receipt and coordinator state

After a checkpoint passes validation, write a small durable receipt containing:
- checkpoint filename/path;
- SHA-256;
- validation status;
- phase/unit;
- completion timestamp;
- high-level counts;
- next authorization state.

A coordinator-state document should point to the **latest validated checkpoint**, not merely the latest working directory.

Do not authorize the next unit automatically unless the research plan explicitly permits it.

---

## 19. Conversation/session rollover

When a conversation reaches maximum length or must be replaced:

- flush all durable state;
- create a checkpoint where practical;
- start fresh from the latest validated artifact;
- do not require the old transcript.

**File continuity is mandatory. Conversation continuity is optional.**

---

## 20. Packaging, storage growth, and validation requirements

For every immutable checkpoint/release:

- use a distinct versioned name;
- do not overwrite predecessor artifacts;
- include a manifest;
- include hashes and byte counts;
- include row counts/schema metadata for structured files where useful;
- include validator or reproducibility scripts when feasible;
- include explicit handoff/state;
- independently reopen and validate the archive.

For deterministic packaging, normalize ZIP timestamps/order when practical.

### 20.1 Exclude runtime debris

Exclude from sealed artifacts unless explicitly required:
- `__pycache__/`;
- `*.pyc`;
- transient browser/cache directories;
- temporary extraction directories;
- packaging scratch files;
- duplicate predecessor ZIPs;
- duplicate baseline extraction trees;
- other reproducible runtime debris.

### 20.2 Storage-growth audit before sealing

Before accepting a checkpoint/release, calculate where practical:
- proposed archive file count;
- compressed/uncompressed size;
- bytes by major category;
- duplicate-content SHA-256 groups;
- duplicate-byte total;
- nested archive count;
- predecessor-checkpoint ZIP count;
- duplicated baseline bytes;
- raw-evidence duplicate bytes;
- largest files;
- growth ratio versus predecessor.

Stop and investigate unexplained superlinear growth, large duplicate groups, or recursive archive chains.

### 20.3 Operational checkpoint dependency validation

An operational checkpoint validator should report separately:
1. **internal archive integrity**; and
2. **external dependency integrity**.

If a declared dependency is unavailable, report a dependency condition such as:

`EXTERNAL_DEPENDENCY_UNAVAILABLE`

Do not mislabel missing external assets as internal archive corruption.

### 20.4 Portable-release validation

A portable release must not rely silently on undeclared external files. Validate the self-contained package (or explicitly paired evidence bundle) after packaging.

---

## 21. Recommended directory pattern

This is a generic example, not a required path:

```text
project/
  00_baselines/
  00_PROJECT_CONTROL/
  01_recovery/
  02_working/
  03_checkpoints/
  04_releases/
  05_raw_captures/
  99_logs/
```

Project-specific paths may differ.

Keep:
- immutable baselines separate from working files;
- checkpoints separate from releases;
- raw captures independently identifiable;
- coordinator metadata small and durable.

---

## 22. Stop conditions

Stop substantive work when:
- durable writes fail;
- integrity discrepancy makes the predecessor uncertain;
- authorized scope is complete;
- search budget is exhausted;
- approaching execution limits requires emergency checkpointing;
- a project-specific safety/methodological boundary is reached.

Do not continue merely because unused time or budget remains.

---

## 23. Anti-patterns

Never:
- trust hidden workspace persistence as the sole copy;
- use progress narration as recovered evidence;
- rerun research before reconciling surviving files;
- overwrite lost search rows with recovery results;
- regenerate missing evidence from memory;
- claim a reconstructed selection is identical without proof;
- perform full historical validation at every startup without cause;
- spend high-cost judgment-model capacity on deterministic hash/schema/manifest checks when a workhorse can validate them;
- skip full validation when sealing a new artifact;
- start the next micro-batch before the current checkpoint is durable and validated;
- silently mutate predecessor ZIPs;
- recursively embed predecessor checkpoints when cryptographic ancestry is sufficient;
- copy large immutable baselines/evidence into every working batch without necessity;
- let a workhorse model silently resolve ambiguity outside frozen rules;
- let a judgment model directly perform large deterministic materialization when a frozen decision ledger can be replayed;
- rerun evidence acquisition merely because metadata integrity disagrees before determining whether the bytes or the metadata are wrong;
- conflate checkpoint completion with phase completion.

---

---

## 25. Capability-tiered execution

Model selection should follow **epistemic difficulty**, not whole-phase habit or model prestige.

Define generic roles rather than hard-coding model names.

### 25.1 Recommended capability classes

Use a scale such as:

- **J0 — deterministic:** hashing, manifests, schema checks, exact row transformations, packaging.
- **J1 — extraction/structured transformation:** source metadata extraction, frozen-query execution, staging claims, table reshaping.
- **J2 — bounded interpretation under explicit rules:** apply a frozen skip condition, classify against a closed rubric, map known values.
- **J3 — substantive evidentiary judgment:** source independence, conflicting-fact resolution, actor responsibility, inclusion/status decisions.
- **J4 — methodological judgment:** protocol changes, stopping rules, design changes, ambiguous recovery policy.

Default routing:

- J0–J1 -> **workhorse role**
- J2 -> workhorse if rules are explicit and closed; otherwise judgment role
- J3–J4 -> **judgment role**
- unusual disagreement/failure -> optional **escalation/audit role**

Actual model names belong in a project configuration file, not the normative skill.

See `templates/MODEL_ROLE_MAP_TEMPLATE.json`.

### 25.2 Judgment budget is a protected resource

Do not spend judgment-model budget on deterministic integrity verification. All J0/J1 continuity work belongs to the workhorse tier unless an explicit audit exception is recorded.

Do not spend judgment-model capacity on:
- hashes;
- CRC;
- row counts;
- byte lengths;
- schemas;
- manifest validation;
- archive traversal;
- deterministic packaging;
- bulk provenance row generation;
- deterministic source-ID allocation;
- mechanical queue/status updates.

This also includes Git state, branch identity, capture accounting, ID accounting, reference integrity, ZIP validation, LFS checks, CI readiness, and construction of a compact decision packet.

A workhorse should validate and prepare these inputs first.

The judgment role should consume a compact, validated decision packet and should not traverse the full filesystem or rerun attested mechanical checks merely to rediscover the workspace.

The authority boundary is normative:

> A lower-cost or lower-authority model may detect ambiguity, but it must not silently resolve ambiguity outside explicit frozen rules.

When an unplanned ambiguity is encountered, flag it, preserve the evidence, continue only unaffected work, and escalate it to the authorized judgment tier.

---

## 26. Frozen inter-model handoffs

Every model-role transition should be mediated by durable artifacts, not only prose in chat.

Before substantive execution at every stage:

1. preserve the exact invocation prompt;
2. hash it;
3. create or append a machine-readable run record with model, skill-dependency, runtime, branch, and scope provenance;
4. commit and push that provenance;
5. only then begin substantive work.

Prompt provenance is append-only. A correction prompt is a separate prompt and correction event; it never overwrites the original prompt or rewrites historical commits.

Recommended pattern:

1. **Preparation handoff** — inherited evidence packets and material gaps.
2. **Frozen search plan** — exact queries, budgets, skip rules, extraction requirements.
3. **Acquisition handoff** — retained sources, claims staging, capture index, coverage matrix.
4. **Readiness attestation** — deterministic integrity PASS before judgment.
5. **Frozen adjudication ledger** — source and fact decisions.
6. **Materialization ledger** — deterministic application of decisions.
7. **Validated checkpoint** — resumable successor.

The receiving model should rely on the frozen artifact and should not silently broaden its authority.

### 26.1 Workhorse ambiguity boundary

A workhorse may **detect** ambiguity but must not resolve it outside an explicit frozen rule.

Use a state such as:

`BLOCKED_REQUIRES_JUDGMENT`

Record:
- item/decision ID;
- exact ambiguity;
- evidence involved;
- why mechanical application is impossible.

Continue independent mechanically safe work where allowed, but do not guess.

---

## 27. Judgment-only adjudication and deterministic materialization

For structured verification projects, prefer a split analogous to:

`prepare -> plan -> acquire -> judge -> materialize -> package`

The names/stage letters are project-specific; the authority boundary is the important part.

### 27.1 Judgment stage

The judgment role should:
- decide source acceptance/independence;
- resolve or preserve conflicts;
- decide exact authoritative values/statuses;
- assign change types;
- specify supporting staged source/claim IDs;
- record limitations/follow-up needs.

It should write a machine-readable **decision ledger**.

It should not, by default:
- allocate hundreds of authoritative IDs;
- generate large provenance tables;
- apply queue/status bookkeeping;
- package the checkpoint.

### 27.2 Decision ledger contract

Each decision should include enough information for deterministic replay, such as:
- decision/target ID;
- entity type and ID;
- field;
- current value;
- action;
- decided value;
- evidence status;
- change type;
- supporting staged source IDs;
- supporting staged claim IDs;
- contradicting source IDs where relevant;
- attribution requirement;
- limitation/reason;
- materialization-required flag.

Typical actions:
- `KEEP`
- `CHANGE`
- `PRESERVE_CONFLICT`
- `SET_UNKNOWN`
- `SET_NOT_FOUND`
- `DEFER_FOLLOWUP`

If a workhorse would need to infer what the judgment model meant, the decision record is not specific enough.

See `templates/ADJUDICATION_DECISION_TEMPLATE.json`.

### 27.3 Per-item durable judgment commits

Expensive judgment work should be committed in bounded durable units (for example, per case/item).

After each completed item:
- write the decision artifact;
- hash it;
- write a commit record;
- mark the item complete.

A quota/context interruption should not force completed judgment items to be adjudicated again.

See `templates/JUDGMENT_COMMIT_TEMPLATE.json`.

### 27.4 Materialization stage

The workhorse should:
- allocate deterministic IDs;
- promote accepted sources;
- write links/independence rows;
- generate provenance;
- apply controlled changes;
- update statuses/queues;
- write a materialization ledger;
- produce a diff/audit.

Every frozen decision must map to exactly one materialization result.

If application requires substantive interpretation, use:

`D2_BLOCKED_REQUIRES_JUDGMENT`

and return that item to the judgment tier.

See `templates/MATERIALIZATION_LEDGER_TEMPLATE.csv`.

---

## 28. Workhorse-owned readiness and integrity gates

Before expensive judgment work, a workhorse should perform deterministic integrity checks and produce a compact **readiness attestation**.

The attestation may cover:
- predecessor identity;
- frozen-plan identity;
- search/capture accounting;
- capture hashes;
- staging row counts;
- target/source ID uniqueness;
- protected authoritative-table hashes;
- absence of unauthorized modifications;
- exact current stage.

For substantive judgment, prefer a machine-readable `JUDGMENT_READINESS_ATTESTATION.json` that also records expected case/item scope, frozen search/acquisition state, evidence availability, target count, protected authoritative-state hashes, packet completeness, unresolved ambiguity flags, allowed judgment scope, and any clarification reserve.

The judgment role should verify the identity of the attestation and decision packet, then normally **trust a PASS attestation** rather than recomputing the same hashes/counts.

Escalate only if:
- the attestation reports a discrepancy;
- the judgment inputs contradict the attestation;
- an explicit independent audit is requested.

See `templates/JUDGMENT_READINESS_ATTESTATION_TEMPLATE.json`.

---

## 29. Integrity mismatch: repair before reacquisition

An integrity mismatch does **not** automatically authorize repeating research.

First determine whether the problem is:
- raw-byte corruption/mutation;
- missing evidence;
- path/reference mismatch;
- derived metadata error;
- transcription error;
- unresolved.

Recommended reconciliation:

1. stop downstream adjudication/materialization;
2. preserve the original failed integrity record;
3. independently recompute hashes/identity;
4. locate all metadata references;
5. look for independently retained byte copies;
6. verify structural identity of the retained object;
7. classify the discrepancy.

If retained bytes are intact and the defect is metadata-only:
- preserve original erroneous metadata in historical repair provenance;
- correct current derived metadata;
- do not change raw evidence bytes;
- rerun the deterministic integrity gate;
- resume only after PASS.

If raw bytes may have changed or identity is unresolved:
- do not silently repair;
- do not rerun the search automatically;
- stop for coordinator/judgment review.

Replacement research still requires explicit authorization and new IDs/budget under Section 12.

See `templates/INTEGRITY_RECONCILIATION_TEMPLATE.json`.

---

## 30. Operational storage architecture

Use distinct storage roles where practical:

1. **Canonical baseline** — immutable starting corpus/releases.
2. **Canonical evidence store** — retained raw source bytes, preferably hash-indexed/content-addressed.
3. **Working state** — mutable current unit, staging, scripts, derived files.
4. **Operational checkpoints** — compact resumable cumulative structured state + dependency ledger.
5. **Portable releases** — self-contained milestone artifacts, flattened/deduplicated.

Recommended external-dependency metadata is in `templates/EXTERNAL_DEPENDENCIES_TEMPLATE.json`.

The current accepted cumulative structured state belongs directly in Git. Do not create recursive `v01/v02/v03/...` copies of the same cumulative tables. Historical accepted states are recovered through Git history and tags.

For immutable evidence, prefer a content-addressed store such as:

`evidence/objects/sha256/<prefix>/<sha256>.<ext>`

Maintain an evidence index mapping each logical identity to its SHA-256, byte length, case/item, search or acquisition ID, source ID, legacy path when applicable, current Git path, and required/optional status. Use Git LFS for large or binary artifacts when configured and appropriate; an LFS pointer alone does not prove that the intended object is available.

### 30.1 Cryptographic ancestry, not recursive bytes

A successor operational checkpoint should usually retain:
- predecessor ID;
- canonical project-relative path;
- SHA-256;
- byte length;
- validation status.

It should not normally retain the predecessor ZIP bytes themselves.

### 30.2 Project-relative dependency paths

Prefer project-relative dependency paths so the durable project tree may move as a unit.

Absolute paths may be recorded as convenience metadata but should not be the sole locator.

### 30.3 Validator semantics

For operational checkpoints, validators should distinguish:
- `internal_archive_integrity`;
- `external_dependency_integrity`;
- `operational_checkpoint_readiness`.

This prevents a missing external canonical asset from being confused with a corrupt ZIP.

---

## 31. Optional operations telemetry

Operations telemetry may be recorded to improve batch sizing and model routing.

Examples:
- stage/unit;
- model role;
- actual model name;
- reasoning level;
- wall-clock duration;
- usage meter before/after if available;
- searches/items/decisions;
- interruption count.

This metadata is **not research evidence** and must not influence substantive findings.

Use it only to improve execution efficiency and reliability.

See `templates/OPERATIONS_TELEMETRY_TEMPLATE.json`.

---

## 32. Minimal operational checklist

Before work:
- identify predecessor + SHA;
- lightweight identity/state check;
- confirm durable storage;
- fix scope/budget/IDs;
- initialize execution status;
- classify tasks by capability tier;
- choose workhorse/judgment roles from project model mapping.

During work:
- existing evidence first;
- log exact queries;
- preserve captures;
- persist stage-boundary artifacts;
- keep non-authoritative staging separate from authoritative state;
- commit expensive judgment work in bounded durable units;
- update status frequently.

Before judgment-model work:
- workhorse validates deterministic integrity;
- produce a readiness attestation;
- provide a compact reading/index bundle;
- avoid making the judgment model re-run hashes, row counts, manifests, or archive validation.

During adjudication:
- judgment model records structured decisions;
- do not require it to expand those decisions into large authoritative tables;
- persist decisions item/case by item/case.

During materialization:
- workhorse replays frozen decisions mechanically;
- stop any item requiring new substantive interpretation;
- emit a materialization ledger linking each frozen decision to its applied result.

Before limits:
- stop acquisition;
- flush state;
- emergency checkpoint.

At unit completion:
- derive summaries;
- run storage-growth/duplication audit;
- package non-recursively where appropriate;
- independently validate internal integrity;
- validate declared external dependencies;
- write receipt/coordinator state;
- stop.

At phase completion:
- run project-specific full integrity suite;
- produce immutable portable release or explicitly declared operational checkpoint;
- independently validate;
- hand off to next phase.

---

## 33. Git-native authority and promotion

Git is part of the research governance boundary, not merely a transport mechanism.

### 33.1 Authoritative branch

The authoritative branch is usually `main`. It should be protected and contain accepted state only. Execution agents must not write to it directly, force-push it, delete it, or bypass its required review and CI controls.

The current authoritative branch head is obtained from Git/GitHub. It should not be copied into self-referential metadata that is changed by the same commit.

### 33.2 Execution branches

Workhorse and judgment agents may create bounded execution branches such as `phase2/unit-A`, `migration/post-baseline`, or `skill/<change>`. They may commit and push those branches within their authorization. A branch name is not evidence that the branch is accepted.

### 33.3 Pull-request promotion boundary

A pull request must expose every proposed authoritative change, preserve commit history, carry CI and validator results, and remain unmerged until explicit approval. The coordinator reviews the actual diff and logs. The human owner performs the final merge under the repository's protected-branch rules.

### 33.4 Trusted-base plus candidate validation

A proposed branch must not be able to weaken its own validator and thereby evade the governance policy that governed its starting state. When practical, CI runs:

1. the validator trusted by the pull-request base commit; and
2. the validator proposed by the candidate branch.

This is monotonic validation: a pull request may strengthen future validation, but it cannot evade the base policy merely by editing the candidate validator. Workflow files and validation trust roots should be protected more strongly than ordinary research files where practical.

### 33.5 Validator observability

A validator must not merely exit successfully. Important sections must emit explicit telemetry so silently skipped checks are detectable. Use statuses such as:

- `status_distribution=PASS`;
- `referential_integrity=PASS`;
- `provenance_references=PASS`;
- `historical_loss_firewall=PASS`.

Validation frameworks must distinguish a check that executed and passed, executed and failed, was skipped, or lacked a prerequisite. A silent no-op check is a defect.

### 33.6 Self-reference-safe Git metadata

Do not store the SHA of the commit containing a metadata record inside that same record. Use fields such as `recorded_through_commit`, `metadata_commit_self_excluded: true`, and `commit_list_scope`. Obtain the current branch or PR head from Git/GitHub. Do not create infinite metadata-update loops.

### 33.7 Model, skill, and runtime provenance

Every substantive run records the model at the level actually known:

- `model_ui_label`;
- `backend_model_identifier` (use `unavailable` when not exposed);
- `model_role`;
- `configuration`.

It also records custom-skill dependencies separately from runtime capabilities. If a custom skill was invoked, record its repository, commit, path, version, and identity hash as available. If none was invoked, record an empty list. Never infer use merely because a skill exists nearby. OpenAI or backend-provided runtime skills are external runtime dependencies, not user-controlled skill artifacts.

Runtime provenance may separately identify the execution environment, Git, Git LFS, GitHub CLI or connector, and explicitly authorized public web access. Do not invent unavailable backend identifiers.

### 33.8 Dedicated execution identities

Where practical, use a separate machine or bot identity with minimum repository permissions. Routine execution should have no repository-administration, force-push, direct protected-branch, or workflow-edit authority unless explicitly required. Human ownership remains the final governance control. Do not hard-code a project-specific account into this generic skill.

## 34. Git micro-checkpoints and correction workflow

Substantive work should be committed and pushed in bounded units. Examples include infrastructure preparation, search-plan freeze, an evidence-acquisition batch, one adjudicated case/item, deterministic materialization, and validation/reporting. A pushed commit is a durable external checkpoint; a local unpushed commit or chat progress message is not.

For multi-case or multi-item judgment, prefer:

`readiness gate -> judgment item -> commit/push -> next item -> materialization`

Completed judgments must not remain only in model context. The workhorse may materialize frozen decisions, but it must stop and escalate if application requires substantive interpretation.

If a coordinator review finds a defect:

1. coordinator submits `REQUEST CHANGES`;
2. executor receives an explicit correction prompt;
3. correction prompt and event are preserved separately;
4. historical commits are not rewritten;
5. the fix is a new commit;
6. CI reruns;
7. coordinator re-reviews and may replace the blocking state with approval;
8. the human owner performs the final merge.

An infrastructure-only correction does not re-adjudicate research conclusions unless that scope is explicitly authorized.

See the run, prompt, correction, handoff, and trusted-validation templates for machine-readable forms.
