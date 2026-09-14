# SKILL — Bitmap Subtitle Transcription / Conversion

## Trigger

Use this skill when the user wants to:
- transcribe bitmap subtitles;
- convert PGS/VobSub subtitles to SRT or another text format;
- prepare a title for bitmap-subtitle OCR/transcription;
- inspect/extract native English bitmap subtitle tracks.

## Governing workflow

1. Explain the proposed preparation workflow and safety boundaries.
2. Obtain approval unless the user already explicitly requested execution.
3. Provide a fresh self-contained PowerShell preparation script for the current title/task.
4. Detect required tools and report missing dependencies clearly.
5. Inspect the source media.
6. Prefer native English bitmap subtitle tracks.
7. Extract directly:
   - PGS -> `.sup`
   - VobSub -> `.idx` + `.sub`
8. Do not default to Subtitle Edit bitmap export.
9. Preserve a task manifest and preparation report.
10. Transcribe/convert with timing fidelity and uncertainty tracking.
11. Validate output before calling the task complete.

## Dependency behavior

For MKV sources, prefer MKVToolNix:
- `mkvmerge`
- `mkvextract`

Detect tools in:
- PATH;
- common installed locations;
- reasonable portable locations near the script.

Subtitle Edit:
- detect an installed copy if present;
- detect a user-supplied portable copy if present;
- do not require it for native extraction;
- do not silently download or install it.

If a required dependency is missing, stop cleanly and report exactly what is missing.

## Source safety

The preparation script must:
- read the source media;
- never modify the source in place;
- create a separate output directory;
- avoid deleting user media;
- avoid overwriting extracted assets unless explicitly allowed;
- avoid network downloads by default.

## Language selection

Prefer subtitle tracks explicitly tagged English (`eng`, `en`, or equivalent metadata).

If multiple English bitmap tracks exist:
- enumerate them;
- preserve track IDs and names;
- do not silently guess which one the user wants when the distinction matters (e.g. full vs forced / SDH vs non-SDH).

## Transcription principles

- Do not invent missing dialogue.
- Preserve timestamps faithfully.
- Repair timing only when the evidence supports it.
- Flag ambiguous OCR/transcription.
- Keep speaker labels, signs, and non-speech cues only when supported by the bitmap subtitles.
- Validate monotonic timestamps and obvious persistence/end-time errors.

## Fresh-script requirement

When the user asks to prepare a new title, provide the preparation script anew rather than referring to a copy from a prior conversation.
