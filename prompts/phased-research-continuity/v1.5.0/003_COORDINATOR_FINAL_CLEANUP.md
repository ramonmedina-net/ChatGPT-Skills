# Coordinator Final Cleanup — Phased Research Continuity v1.5.0

Coordinator re-review found only two final cleanup items on PR #1.

Resume the existing branch:

skill/phased-research-continuity-v1.5.0

Do not recreate the branch, amend/rewrite prior commits, force-push, merge the PR, or modify Filicide-Research.

Preserve this follow-up correction instruction as append-only provenance if the current v1.5.0 correction workflow requires it.

1. Finish Git-native/artifact-native checkpoint consistency in SKILL.md.

The new Section 5 checkpoint modes are correct, but several older passages remain artifact-centric.

Update them so:

- Section 17 explicitly distinguishes Git-native operational checkpoints from artifact-native operational checkpoints. Manifest/archive requirements apply only where an artifact/archive exists.

- Section 18 makes the checkpoint receipt mode-aware:

  - Git-native: execution branch + pushed commit identity + validation/handoff/provenance;
  - artifact-native: filename/path + SHA-256 + byte length + validation;
  - portable release: sealed artifact identity and independent package validation.

- Section 27 changes the example structured workflow from:

  prepare -> plan -> acquire -> judge -> materialize -> package

  to a mode-neutral form such as:

  prepare -> plan -> acquire -> judge -> materialize -> checkpoint -> package_if_required

- Scan nearby lifecycle/checklist language for any remaining statement that accidentally requires ZIP/archive packaging for every Git-native micro-checkpoint.

Do not weaken archive validation for artifact-native checkpoints or portable releases.

2. Finalize correction-run provenance.

The existing:

runs/phased-research-continuity/v1.5.0/CORRECTION-1.5.0-001.json

currently records only correction startup state.

Finalize it, or add a separate append-only completion event if that is cleaner.

Record accurately:

- correction commits:
  - 86ce40e
  - 43911c0
- deterministic package build: PASS
- two-build deterministic SHA-256 match:
  285110221d307e6b60359a6d5c291147f84c7ba0109abee8b1ff5989addb79c9
- package validation: PASS
- GitHub CI/checks: NOT_CONFIGURED (or equivalent explicit state), not blank and not PASS
- coordinator re-review result at the recorded-through point: CHANGES_REQUESTED_PENDING_FINAL_CLEANUP or equivalent accurate state
- substantive scope changed: false
- research re-adjudication: false
- correction completed: true/status completed

Use self-reference-safe semantics:

- recorded_through_commit
- metadata_commit_self_excluded: true

Do not try to record the SHA of the metadata-bearing commit itself.

3. Rebuild and validate.

Run the deterministic builder twice and confirm identical SHA-256.

Run validate_package.py on the resulting package.

Update PACKAGE_MANIFEST.json if any packaged bytes changed.

Confirm:

- package validation PASS;
- no unrelated files changed;
- no Filicide-Research changes;
- no secrets/runtime debris;
- VERSION remains 1.5.0.

Commit and push normally as new commits.

PR #1 stays open and unmerged.

Final response should report:

- new commits;
- checkpoint-language cleanup;
- correction provenance completion;
- deterministic build hashes;
- package validator result;
- current PR head;
- PR #1 open/unmerged;
- ready for final coordinator re-review.

Then stop.
