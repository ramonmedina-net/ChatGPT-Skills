# ChatGPT Skills

Reusable skill packages for ChatGPT workflows and long-running projects.

Each skill lives under [`skills/`](./skills/) and includes its own operating instructions, documentation, package metadata, and supporting templates/scripts where applicable.

## Skills

### [Phased Research Continuity](./skills/phased_research_continuity_skill/)

**Current version:** 1.4.0 — *Storage Architecture & Capability-Tiered Execution*

A continuity and execution framework for complex, multi-session research programs that need durable checkpoints, bounded search budgets, provenance, reproducibility, recovery after interruption, and efficient division of labor between high-volume workhorse models and higher-cost judgment models.

Key capabilities include:
- immutable predecessor and checkpoint discipline;
- non-recursive operational checkpoints with cryptographic ancestry;
- external dependency ledgers and storage-growth audits;
- J0–J4 capability-tiered model routing;
- frozen inter-model handoffs;
- judgment-only adjudication followed by deterministic materialization;
- integrity reconciliation before reacquiring evidence;
- micro-batch execution, recovery, and durable handoff rules.

Start with [`SKILL.md`](./skills/phased_research_continuity_skill/SKILL.md). The directory also contains `README.md`, `LLM_INSTRUCTIONS.md`, `CHANGELOG.md`, `PACKAGE_MANIFEST.json`, `VERSION`, validation tooling, and reusable templates.

### [Bitmap Subtitle Transcription / Conversion](./skills/bitmap_subtitle_transcription_skill/)

**Current version:** 1.0.0

A workflow for preparing, extracting, transcribing, and converting bitmap subtitle tracks while preserving source media and timing fidelity.

Key capabilities include:
- direct extraction of native English bitmap subtitle tracks;
- PGS (`.sup`) and VobSub (`.idx` + `.sub`) workflows;
- fresh self-contained PowerShell preparation scripts per task;
- dependency detection without silent installation/downloads;
- source-preservation safeguards;
- timing, OCR/transcription uncertainty, and output validation.

Start with [`SKILL.md`](./skills/bitmap_subtitle_transcription_skill/SKILL.md). The directory also contains `README.md`, `LLM_INSTRUCTIONS.md`, `TASK_INSTRUCTIONS.md`, `PACKAGE_MANIFEST.json`, plus supporting `scripts/` and `templates/`.

## Repository layout

```text
ChatGPT-Skills/
├── README.md
└── skills/
    ├── bitmap_subtitle_transcription_skill/
    └── phased_research_continuity_skill/
