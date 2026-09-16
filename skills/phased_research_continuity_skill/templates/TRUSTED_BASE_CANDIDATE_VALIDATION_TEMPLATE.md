# Trusted-Base / Candidate Validation Checklist

## Pull request
- Base branch:
- Base commit:
- Candidate branch:
- Candidate head:
- Pull request:

## Trusted validator
- Validator path at base commit:
- Base validator identity/hash:
- Base validator executed: PASS|FAIL|SKIPPED|PREREQUISITE_MISSING
- Base-validator result:

## Candidate validator
- Validator path at candidate head:
- Candidate validator identity/hash:
- Candidate validator executed: PASS|FAIL|SKIPPED|PREREQUISITE_MISSING
- Candidate-validator result:

## Observability
- status_distribution=PASS|FAIL|SKIPPED|PREREQUISITE_MISSING
- referential_integrity=PASS|FAIL|SKIPPED|PREREQUISITE_MISSING
- provenance_references=PASS|FAIL|SKIPPED|PREREQUISITE_MISSING
- historical_loss_firewall=PASS|FAIL|SKIPPED|PREREQUISITE_MISSING

## Review gate
- No candidate change weakens the base validation policy:
- CI logs attached:
- Coordinator review:
- Human final merge required: true
