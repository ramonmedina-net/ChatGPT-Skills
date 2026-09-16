Coordinator review has requested changes on PR #1.

Resume the existing branch:

`skill/phased-research-continuity-v1.5.0`

Do not recreate the branch, do not rewrite or amend existing pushed commits, do not force-push, do not merge the PR, and do not modify Filicide-Research.

Preserve this correction invocation as a separate append-only prompt/run event before substantive corrections, consistent with the new v1.5.0 provenance doctrine.

Address exactly these coordinator findings:

## 1. Active execution-branch resume authority

Clarify the authority model so accepted state and resumable proposed state are distinct.

Add a normative rule equivalent to:

> The protected authoritative branch remains the accepted research state. Within an already-authorized active execution unit or open pull request, however, the latest validated and pushed execution-branch checkpoint is the authoritative resume point for that proposed work. It does not supersede accepted state until promotion/merge.

Ensure interruption/recovery guidance uses that rule so a fresh executor resumes an active unit from its latest durable pushed checkpoint rather than restarting from older `main`.

Update templates/LLM instructions where needed.

## 2. Reconcile artifact-native and Git-native checkpoint lifecycles

The older unit lifecycle still implies that every bounded execution unit must package an immutable checkpoint archive.

v1.5.0 now also defines pushed Git commits as durable micro-checkpoints.

Reconcile these without removing support for non-Git/artifact-native workflows.

Define at least:

### Git-native operational checkpoint

A validated pushed commit on the authorized execution branch, accompanied by sufficient run state/provenance/handoff/validator evidence, may serve as the durable operational checkpoint for continued work.

It does NOT require a ZIP/archive at every case, stage, or micro-batch.

### Artifact-native operational checkpoint

For non-Git workflows, or projects that explicitly require sealed artifacts, retain the existing immutable checkpoint/archive workflow.

### Portable release / explicit sealing milestone

Continue to require explicit packaging and independent archive validation where portability, release sealing, migration, or project policy requires it.

Update the generic unit lifecycle/checklists so they do not require both Git commit checkpointing and ZIP packaging for every bounded unit.

## 3. Deterministic cross-platform skill packaging

The build run recorded:

`working_tree_package = FAIL_PREEXISTING_CRLF_CHECKOUT_MISMATCH`

because the Windows checkout has `core.autocrlf=true`, while the canonical Git-blob package uses LF and validates.

Do not leave this as an undocumented packaging hazard.

Implement a deterministic supported packaging method.

Preferred solution:

- add a deterministic package-builder script under the skill, e.g. `build_package.py`;
- package canonical bytes in a platform-independent way;
- normalize intended text package members to LF or read canonical Git blobs deterministically;
- use deterministic file ordering;
- use deterministic ZIP metadata/timestamps where practical;
- exclude `PACKAGE_MANIFEST.json` from self-hashing according to existing policy;
- ensure the resulting package exactly matches `PACKAGE_MANIFEST.json`;
- document the supported build command in README/SKILL;
- validate the produced ZIP with `validate_package.py`.

If `.gitattributes` is also useful, add only the minimal repository normalization necessary and do not disturb the unrelated bitmap-subtitle skill.

The build and validator must produce the same valid package semantics on Windows and Linux regardless of `core.autocrlf`.

Preserve the historical preflight record showing the CRLF mismatch; do not rewrite history.

## 4. Preserve generic applicability

Scope statements such as:

`current accepted cumulative structured state belongs directly in Git`

to Git-native projects where repository policy, data classification/sensitivity, storage size, and technical constraints permit it.

For projects where authoritative structured data cannot appropriately live in Git, permit:

- an external authoritative structured store;
- Git-tracked schema/manifests/indexes;
- immutable snapshot identity;
- hashes/version IDs;
- explicit durable locators;
- validated dependency records.

Do not weaken the Git-native architecture for projects such as Filicide-Research; simply avoid making direct Git storage mandatory for every possible research program.

Apply this clarification consistently to SKILL.md, LLM_INSTRUCTIONS.md, README.md, CHANGELOG.md, and relevant templates if needed.

## Validation

After corrections:

- update VERSION only if necessary; target remains `1.5.0`;
- update PACKAGE_MANIFEST.json hashes/byte counts;
- build the package through the new deterministic supported method;
- run `validate_package.py` against that produced package;
- ensure validation PASS;
- verify prompt/run correction provenance;
- verify no Filicide-Research changes;
- verify no secrets/runtime debris;
- verify the existing v1.5.0 features remain intact.

Add corrections as new commits and push normally.

Update PR #1 in place.

Do not merge.

Final response should report:

- correction commits;
- active-branch resume-rule result;
- Git-native vs artifact-native checkpoint reconciliation;
- deterministic package-builder/normalization result;
- generic external-store fallback result;
- package build result;
- package validation result;
- current PR head;
- PR #1 open/unmerged;
- ready/not ready for coordinator re-review.

Then stop.