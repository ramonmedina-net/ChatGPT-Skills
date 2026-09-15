# Phased Research Continuity — v1.5.0 Git-Native Governance Update

## Role

You are updating the custom skill:

**Phased Research Continuity**

Repository:

`ramonmedina-net/ChatGPT-Skills`

Current authoritative version:

`v1.4.0`

Target version:

`v1.5.0`

This is a **skill-engineering and repository-governance task**, not filicide research.

Do not conduct case research, web evidence discovery, or modify the Filicide-Research repository.

The purpose of v1.5.0 is to incorporate the empirically validated Git-native research architecture learned during the post-B04 migration of:

`ramonmedina-net/Filicide-Research`

Preserve all useful v1.4.0 behavior unless intentionally superseded.

---

# 1. Execution identity and repository preflight

Use the GitHub execution identity:

`ramon-auto`

Before modifying anything:

```powershell
gh auth status
git --version
git lfs version
```

Locate the local clone of:

`ramonmedina-net/ChatGPT-Skills`

If no clone exists in the authorized local workspace, clone it into an appropriate persistent local folder.

Then:

```powershell
git status
git branch --show-current
git fetch origin
git switch main
git pull --ff-only
git rev-parse HEAD
git rev-parse origin/main
```

Requirements:

- authenticated GitHub user = `ramon-auto`;
- `main` clean;
- local `main` aligned with `origin/main`;
- no uncommitted unrelated changes.

Do not reset, delete, or overwrite unexpected work.

If the repository state is materially unexpected, STOP and report it.

---

# 2. Current skill identity

Read the current authoritative v1.4.0 skill from:

`skills/phased_research_continuity_skill/`

At minimum inspect:

- `SKILL.md`
- `LLM_INSTRUCTIONS.md`
- `README.md`
- `CHANGELOG.md`
- `VERSION`
- `PACKAGE_MANIFEST.json`
- `validate_package.py`
- all templates under:
  `skills/phased_research_continuity_skill/templates/`

Confirm current version:

`1.4.0`

Confirm the current skill is internally valid before modification.

Run the existing package validator before making substantive changes and record the result.

Do not silently repair unrelated historical defects. If a pre-existing defect blocks the update, document it explicitly.

---

# 3. Create a governed feature branch

Create:

`skill/phased-research-continuity-v1.5.0`

Do not work directly on `main`.

Do not force-push.

Do not merge the PR.

---

# 4. Preserve this invocation prompt first

Before substantive skill editing, preserve this exact submitted prompt in the repository.

Preferred path:

`prompts/phased-research-continuity/v1.5.0/001_INITIAL_PROMPT.md`

Preserve exact submitted bytes where practical.

Create an append-only run record, for example:

`runs/phased-research-continuity/v1.5.0/BUILD-1.5.0-001.json`

Record at minimum:

- run ID;
- skill name;
- source version;
- target version;
- prompt path;
- prompt SHA-256;
- model UI label: `Luna Max`;
- backend model identifier: `unavailable` unless actually exposed;
- model role: `workhorse`;
- starting Git commit;
- branch;
- start timestamp;
- status;
- custom-skill dependencies actually invoked, if any;
- runtime capabilities used;
- web research: false unless later explicitly authorized.

Commit and push this provenance before substantive editing.

Suggested commit:

`Record Phased Research Continuity v1.5.0 build invocation`

---

# 5. v1.5.0 design objective

v1.5.0 should formalize a Git-native, capability-tiered research execution architecture based on lessons empirically demonstrated during B04 and the post-B04 Git migration.

The normative principle is:

> The model is interchangeable. Authority resides in validated artifacts, governed Git history, explicit decision boundaries, and human-approved promotion—not in which model produced them.

Retain the existing principle:

> The agent is disposable. The durable state is not.

Also add the operational distinction:

> The workhorse proves the inputs are intact. The judgment tier decides what the intact inputs mean. The workhorse applies the decisions.

---

# 6. Git-native authority model

Add a formal Git governance model.

The skill should distinguish at least:

## Authoritative branch

Usually:

`main`

Properties:

- protected;
- no direct execution-agent writes;
- no force pushes;
- no deletion;
- accepted state only;
- promotion occurs through reviewed pull requests.

## Execution branches

Created by workhorse or judgment agents for bounded work.

Examples:

- `phase2/B05-stage-A`
- `phase2/B05`
- `migration/post-B04-baseline`
- `skill/...`

Agents may commit and push to these branches.

Agents must not bypass the protected authoritative branch.

## Pull request

The PR is the **promotion boundary** between proposed state and accepted state.

A PR must:

- expose all proposed authoritative changes;
- carry CI results;
- preserve commit history;
- permit coordinator review;
- remain unmerged until explicitly approved.

## Final merge

The preferred architecture is:

- execution identity creates branch and PR;
- coordinator independently reviews;
- human owner performs final merge.

The coordinator may approve/request changes but should not normally perform the final merge.

Document exceptions only as explicit governance overrides.

---

# 7. Coordinator / executor separation

Formalize two distinct roles.

## Executor

Typical capabilities:

- local filesystem;
- Git branch;
- Git LFS;
- command execution;
- deterministic transformation;
- authorized research acquisition;
- bounded substantive work according to assigned capability tier;
- commits and pushes;
- opens PR.

Executor must not:

- silently widen scope;
- alter protected governance;
- merge its own authoritative work;
- reinterpret prior accepted decisions unless explicitly authorized.

## Coordinator

Typical capabilities:

- independent repository inspection;
- PR diff review;
- commit review;
- CI/log inspection;
- methodological review;
- approval/request-changes;
- next-stage authorization.

The coordinator should evaluate **what actually landed in Git**, not merely trust an executor's final narrative.

---

# 8. Prompt-first provenance

Make prompt preservation normative.

For every substantive execution stage:

1. preserve the exact invocation prompt;
2. hash it;
3. create/update a machine-readable run record;
4. commit and push that provenance;
5. only then begin substantive work.

Prompt provenance should be append-only.

If a coordinator later sends a correction prompt:

- preserve it separately;
- create a correction-event run record;
- never overwrite the original prompt;
- never retroactively rewrite execution history.

Add or update templates to support this.

Recommended templates:

- `RUN_RECORD_TEMPLATE.json`
- `CORRECTION_RUN_EVENT_TEMPLATE.json`
- `PROMPT_PROVENANCE_TEMPLATE.json`

Names may vary if the existing skill has a cleaner convention.

---

# 9. Durable Git micro-checkpoints

Extend the existing durable checkpoint doctrine into Git-native execution.

Substantive work should be committed and pushed in bounded units.

Do not wait until the end of a long run.

Examples:

- infrastructure preparation;
- search-plan freeze;
- evidence acquisition batch;
- one adjudicated case;
- deterministic materialization;
- validation/reporting.

The preferred checkpoint unit should minimize loss if:

- model quota expires;
- Work session crashes;
- desktop app restarts;
- agent context disappears;
- machine process terminates.

A pushed commit is a durable external checkpoint.

A local unpushed commit is not sufficient.

A chat progress message is not a checkpoint.

---

# 10. Judgment-model quota protection

Make the following a normative capability-tier rule:

> Do not spend judgment-model budget on deterministic integrity verification.

All J0/J1 continuity work belongs to the workhorse tier, including:

- file existence;
- hashes;
- byte lengths;
- row counts;
- schemas;
- manifest reconciliation;
- Git state;
- branch identity;
- capture accounting;
- ID accounting;
- reference integrity;
- packaging;
- ZIP validation;
- LFS checks;
- CI readiness;
- decision-packet construction.

The judgment model consumes a validated decision packet.

It should not:

- traverse the full filesystem unnecessarily;
- rerun hashes already attested by the workhorse;
- reconcile routine row counts;
- rebuild manifests;
- spend substantial context locating evidence.

The judgment tier is reserved for epistemically substantive tasks such as:

- source-independence judgment;
- conflicting evidence;
- actor responsibility;
- ambiguous event structure;
- evidentiary sufficiency;
- unresolved source meaning;
- substantive methodological judgment.

---

# 11. Judgment readiness attestation

Formalize a workhorse-produced readiness gate before substantive judgment.

The workhorse should create a machine-readable artifact such as:

`JUDGMENT_READINESS_ATTESTATION.json`

It should attest:

- expected case/item scope;
- frozen search/acquisition state;
- evidence availability;
- capture integrity;
- target count;
- protected authoritative-state hashes;
- packet completeness;
- unresolved ambiguity flags;
- allowed judgment scope;
- available clarification reserve if applicable.

The judgment tier should verify the identity of the attestation and packet, not redo the mechanical integrity work unless the attestation itself is suspect.

Update the existing readiness-attestation template if one already exists.

---

# 12. Decision packets and reading indexes

Require preparation of compact judgment inputs when practical.

A decision packet may contain:

- exact target IDs;
- current accepted values;
- relevant staged claims;
- exact source/capture locators;
- material conflicts;
- scope constraints;
- permitted decision vocabulary;
- clarification reserve;
- reading index;
- evidence coverage matrix.

The goal is to prevent the judgment model from rediscovering the workspace.

---

# 13. Case/item-level judgment commits

Judgment work must be interruption-resilient.

For multi-case or multi-item adjudication, prefer:

- adjudicate one bounded case/item cluster;
- persist its judgment record;
- commit;
- push;
- continue to the next case/item.

A single judgment-model run may process several cases if quota permits, but completed judgments should not remain only in model context.

Example conceptual flow:

- D1-ready gate — workhorse
- D1-case-1 — judgment
- commit/push
- D1-case-2 — judgment
- commit/push
- D1-case-3 — judgment
- commit/push
- D2 — workhorse materialization

This is a recommended pattern, not a mandatory stage naming scheme.

---

# 14. Judgment / materialization separation

Formalize:

## Judgment tier

Produces compact, machine-readable decisions.

It should not mechanically rewrite hundreds of authoritative rows unless those edits themselves require substantive judgment.

## Workhorse materialization tier

Consumes frozen decisions and:

- updates authoritative tables;
- assigns deterministic IDs;
- writes provenance rows;
- writes controlled-change rows;
- updates statuses;
- runs integrity validation;
- commits/pushes the mechanical result.

The workhorse may detect an ambiguity but must not silently resolve an ambiguity outside frozen rules.

Escalate such ambiguity back to judgment.

---

# 15. Capability classes

Retain or formalize capability classes similar to:

### J0 — deterministic integrity
Examples:
- hashes;
- row counts;
- file traversal;
- manifests;
- Git state;
- packaging.

Default: workhorse.

### J1 — deterministic extraction/transformation
Examples:
- source extraction under frozen rules;
- structured staging;
- normalized machine-readable conversion.

Default: workhorse.

### J2 — bounded interpretation under explicit frozen rules
May be delegated to workhorse only when the rule set fully determines the output.

Otherwise escalate.

### J3 — substantive evidentiary judgment
Examples:
- conflicting source interpretation;
- source independence;
- responsibility;
- evidence sufficiency.

Default: judgment model.

### J4 — methodological/protocol-changing judgment

Requires judgment-tier reasoning and generally coordinator review.

The exact names may be adjusted, but preserve the concept.

---

# 16. Authority boundary

Add a strong normative rule:

> A lower-cost or lower-authority model may detect ambiguity, but it must not silently resolve ambiguity outside explicit frozen rules.

When encountering unplanned ambiguity:

- flag it;
- preserve evidence;
- stop or continue only unaffected work;
- escalate to the authorized judgment tier.

Do not convert efficiency routing into weaker evidentiary standards.

---

# 17. Trusted-base + candidate validation

Formalize the CI trust architecture learned from the migration.

A proposed branch must not be able to weaken its own validator and thereby evade governance.

Preferred model:

1. run the validator trusted by the PR base commit;
2. run the validator proposed by the candidate branch.

This creates monotonic validation:

> A PR may strengthen future validation, but it cannot evade the validation policy that governed its starting state merely by editing the candidate validator.

Document that workflow files and validation trust roots should be protected more strongly than ordinary research files where practical.

The exact CI implementation is repository-specific, but the principle belongs in the skill.

---

# 18. Validator observability

Add the lesson from PR #2:

A validator must not merely exit successfully.

Critical sections should provide explicit execution telemetry so silently skipped checks are detectable.

For important validation sections, emit statuses such as:

- `status_distribution=PASS`
- `referential_integrity=PASS`
- `provenance_references=PASS`
- `historical_loss_firewall=PASS`

A validation framework should distinguish:

- check executed and passed;
- check executed and failed;
- check skipped;
- prerequisite missing.

Silent no-op validation is a defect.

---

# 19. Accepted-state storage architecture

Formalize the Git-native storage layers.

## Current accepted structured state

Store current accepted cumulative state directly in Git.

Do not create recursive `v01/v02/v03/...` copies of the same cumulative tables.

Historical accepted states are recovered through Git history and tags.

## Immutable evidence

Use a content-addressed object store where appropriate, e.g.:

`evidence/objects/sha256/<prefix>/<sha256>.<ext>`

Maintain an evidence index mapping identity to:

- SHA-256;
- byte length;
- case/item;
- search/acquisition ID;
- source ID;
- legacy path where applicable;
- current Git path;
- required/optional status.

## Large/binary artifacts

Use Git LFS when configured and appropriate.

Do not assume an LFS pointer alone proves artifact availability; validators should check the repository's intended LFS boundary.

## Ancestry

Represent predecessor checkpoints primarily by cryptographic identity and provenance.

Do not recursively embed predecessor archives unless self-contained portability is an explicit release requirement.

---

# 20. Operational checkpoint vs portable release

Preserve and strengthen the distinction:

## Operational checkpoint

May rely on separately identified immutable dependencies.

Designed for continued work.

Should be compact and non-recursive.

## Portable release

Must be self-contained according to its declared dependency model.

May intentionally include otherwise external objects.

Do not accidentally treat every operational checkpoint as a portable release.

---

# 21. Self-referential Git metadata

Add an explicit rule:

Do not attempt to store the SHA of the commit containing the metadata record as a field inside that same record.

Avoid misleading fields like:

`final_branch_head_commit`

when the metadata commit itself changes the branch head.

Use semantics such as:

- `recorded_through_commit`
- `metadata_commit_self_excluded: true`
- `commit_list_scope`

The current branch/PR head should be obtained from Git/GitHub.

Do not create infinite metadata-update loops.

Update templates accordingly.

---

# 22. Model provenance

Every substantive run should record the execution model accurately at the level actually known.

Preferred fields:

- `model_ui_label`
- `backend_model_identifier`
- `model_role`
- `configuration`

If the backend identifier is unavailable, record:

`unavailable`

Do not invent an internal model identifier.

Do not substitute a generic platform label for the actual user-selected model label.

---

# 23. Custom skill dependency provenance

Every substantive run should explicitly record custom-skill dependency state.

If a custom skill is actually used, record:

- repository;
- repository commit;
- path;
- version;
- tree/blob/hash identity as appropriate.

If no custom skill is invoked, explicitly record an empty dependency list.

If usage cannot be established, record:

`unknown`

Do not infer skill usage merely because a skill exists in a repository or project.

OpenAI/backend-provided runtime skills or hidden platform instructions are external runtime dependencies and must not be vendored or claimed as user-controlled skill artifacts.

---

# 24. Runtime dependency provenance

Where useful, record non-vendored execution dependencies separately, including examples such as:

- OpenAI Work/local execution environment;
- Git;
- Git LFS;
- GitHub CLI;
- GitHub connector;
- public web access if explicitly authorized.

Do not confuse runtime capability provenance with custom-skill provenance.

---

# 25. Bot credential / governance guidance

The skill may include generic guidance for a dedicated execution identity:

- separate machine/bot account where practical;
- minimum required repository permissions;
- no repository administration;
- no force push;
- no direct protected-branch write;
- no workflow-edit permission for routine research execution where practical;
- final governance controlled by human owner.

Do not hard-code `ramon-auto` into the generic skill except as an optional worked example if helpful.

The skill must remain reusable outside this project.

---

# 26. Repository correction workflow

Formalize how coordinator findings are handled.

If a PR review finds defects:

1. coordinator submits `REQUEST CHANGES`;
2. executor receives an explicit correction prompt;
3. correction prompt is preserved separately;
4. correction run/event is append-only;
5. historical commits are not rewritten;
6. fixes are added as new commits;
7. CI reruns;
8. coordinator re-reviews;
9. coordinator may replace the earlier blocking state with approval;
10. human performs final merge.

No research conclusions should be re-adjudicated during an infrastructure-only correction unless explicitly authorized.

---

# 27. Historical-loss firewall

Preserve all v1.4.0 historical-loss protections.

Git migration or reconstruction does not convert:

- chat progress reports;
- missing workspace claims;
- screenshots;
- remembered counts;
- historical status summaries

into recovered evidence.

Loss-provenance remains separate from authoritative research data.

---

# 28. Templates

Review every existing template for compatibility with v1.5.0.

Update existing templates instead of duplicating concepts unnecessarily.

Add templates only where they materially improve reproducibility.

Candidate template additions or revisions may include:

- Git-native run record;
- prompt provenance record;
- correction-run event;
- PR handoff/review checklist;
- judgment readiness attestation;
- judgment decision commit;
- materialization ledger;
- evidence object/index record;
- trusted-base/candidate validation checklist;
- Git micro-checkpoint handoff.

Do not create template bloat.

Every included template should have a clear operational purpose.

---

# 29. Documentation updates

Update coherently:

- `SKILL.md`
- `LLM_INSTRUCTIONS.md`
- `README.md`
- `CHANGELOG.md`
- `VERSION`
- `PACKAGE_MANIFEST.json`
- relevant templates
- `validate_package.py` if validation requirements changed.

`VERSION` must become:

`1.5.0`

The changelog should clearly distinguish what v1.5.0 adds beyond v1.4.0.

Suggested release theme:

**Git-Native Governance & Judgment-Efficient Execution**

Alternative wording is acceptable if clearer.

---

# 30. Keep the skill generic

Although the lessons came from Filicide-Research, v1.5.0 must remain a general-purpose skill for long-running phased research.

Do not bake in:

- filicide case IDs;
- B04/B05-specific table names;
- Ramon-specific filesystem paths;
- specific research conclusions.

Project-specific examples may be included sparingly and clearly labeled as examples, but normative rules must be domain-neutral.

---

# 31. Package integrity

Update `PACKAGE_MANIFEST.json` accurately.

Ensure the manifest matches the actual package contents and hashes according to the skill's established format.

Run:

```powershell
python skills/phased_research_continuity_skill/validate_package.py
```

or the repository's actual established validation invocation.

Validation must PASS.

If the validator needs to be strengthened for new required files/templates, update it deterministically.

Also inspect for:

- missing manifest entries;
- stale hashes;
- stale version references;
- v1.4.0 text that should now say v1.5.0;
- broken template references;
- duplicate concepts;
- internal contradictions.

---

# 32. Review the resulting diff

Before PR creation:

```powershell
git status
git diff --check
git diff origin/main...HEAD
git log --oneline --decorate origin/main..HEAD
```

Confirm:

- no secrets;
- no unrelated repository changes;
- no generated caches;
- no `__pycache__`;
- no `.pyc`;
- version consistently 1.5.0;
- package validation PASS;
- only intended skill/provenance changes exist.

Use bounded commits rather than one giant opaque commit.

Preferred conceptual sequence:

1. record invocation;
2. implement v1.5.0 core doctrine;
3. update templates and package validation;
4. finalize docs/changelog/manifest;
5. record final build validation.

Push each substantive commit.

---

# 33. Pull request

Open a PR:

Head:

`skill/phased-research-continuity-v1.5.0`

Base:

`main`

Title:

`Release Phased Research Continuity v1.5.0`

PR body should include:

## Release

`Phased Research Continuity v1.5.0`

## Theme

Git-native governance and judgment-efficient execution.

## Major additions

Summarize:

- protected authoritative branch;
- executor feature branches;
- PR promotion boundary;
- coordinator/human merge separation;
- prompt-first provenance;
- append-only correction runs;
- durable Git micro-checkpoints;
- capability-tier routing;
- workhorse integrity gate;
- judgment readiness packets;
- judgment/materialization separation;
- case/item-level judgment commits;
- trusted-base plus candidate validation;
- validator observability;
- content-addressed evidence architecture;
- LFS/identity-only ancestry;
- self-reference-safe Git metadata;
- explicit model/skill/runtime provenance.

## Compatibility

State whether v1.4.0 behavior is preserved and identify intentional supersessions.

## Validation

Report package validator result.

## Scope

No filicide research data or research conclusions modified.

Request review from:

`ramonmedina-net`

Do not merge.

---

# 34. Final run record

Finalize the v1.5.0 build run record using non-self-referential Git semantics.

Use:

- `recorded_through_commit`
- `metadata_commit_self_excluded: true`

Do not attempt to record the SHA of the metadata-bearing commit itself.

Record:

- completion timestamp;
- package validation result;
- resulting version;
- changed file count;
- commit list through the last substantive commit;
- PR number;
- PR URL;
- current branch;
- status: completed.

If a final metadata commit is required, push it and allow CI/repository checks to rerun.

---

# 35. Hard-stop conditions

STOP rather than improvise if:

- current skill does not validate before modification;
- repository starting state is dirty or unexpected;
- `main` is not aligned with `origin/main`;
- GitHub authentication is not `ramon-auto`;
- v1.4.0 cannot be identified cleanly;
- manifest format cannot be reproduced safely;
- updating the skill would require guessing historical package identities;
- branch push fails;
- package validation cannot pass without unrelated changes.

Do not bypass governance to finish the task.

---

# 36. Forbidden actions

Do NOT:

- modify Filicide-Research;
- conduct public web research;
- change filicide research data;
- push directly to `main`;
- merge the PR;
- rewrite already-pushed commits;
- force-push;
- change repository governance/rulesets;
- expose credentials;
- vendor hidden/OpenAI-provided runtime skills;
- claim unavailable backend model identifiers;
- claim a custom skill was used unless it actually was.

---

# 37. Final response

Report concisely:

- starting `main` commit;
- branch;
- source version;
- target version;
- commits created;
- major v1.5.0 additions;
- templates added/changed;
- package validation result;
- final substantive commit recorded;
- current PR head;
- PR number and URL;
- whether CI/repository validation passed;
- whether coordinator review is ready.

Then STOP.

Do not merge.