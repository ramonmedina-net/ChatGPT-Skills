# LLM Instructions

You are using the Bitmap Subtitle Transcription / Conversion skill.

## 1. Before execution

Unless the user has already explicitly asked you to run/prepare/extract:

Explain:
- what source file will be inspected;
- which tools will be used;
- that extraction is native/copy-only rather than transcoding;
- which files will be written;
- that the source media will not be modified;
- that no tool will be downloaded silently.

Then obtain approval.

If the user already explicitly asked to execute, do not redundantly ask for approval again.

## 2. Provide a fresh script

For each title/task, give the user a fresh self-contained PowerShell preparation script based on `scripts/Prepare-BitmapSubtitleTask.ps1`.

Do not tell the user to find a prior script from another chat.

## 3. Prefer direct native extraction

For MKV:
- inspect with `mkvmerge -J`;
- identify English bitmap subtitle tracks;
- extract with `mkvextract tracks`.

PGS:
- output `.sup`.

VobSub:
- request extraction to `.idx`; MKVToolNix normally writes the companion `.sub`.

Do not route the native bitmap through Subtitle Edit export merely to obtain images.

## 4. Dependencies

Detect first; do not assume.

Required for normal MKV workflow:
- MKVToolNix (`mkvmerge`, `mkvextract`).

Useful:
- `ffprobe` / FFmpeg for additional inspection.
- Subtitle Edit if installed or supplied portable for later compatible operations.

If tools are missing:
- name the missing executable;
- say what function it is needed for;
- stop without damaging or modifying source files.

## 5. Multiple tracks

If multiple English bitmap tracks exist:
- list track ID;
- codec;
- language;
- track name;
- default/forced flags where available.

If the user's intended track is obvious from an explicit request, use it.
Otherwise ask which track to transcribe before choosing when the distinction is material.

## 6. Output/task manifest

Preserve:
- source path;
- source size;
- extraction timestamp;
- tool paths/versions where available;
- chosen track metadata;
- output file paths;
- codec;
- language.

## 7. Transcription stage

Do not fabricate text.

When reading bitmap subtitles:
- preserve line breaks when meaningful;
- use sensible SRT text normalization;
- retain meaningful non-speech cues if present;
- record uncertain readings for review.

Timing:
- preserve original subtitle event timing;
- do not make arbitrary global offsets;
- repair a malformed end time only when the adjacent subtitle evidence supports the repair.

## 8. Validation

Before calling the conversion complete, check:
- SRT sequence numbers;
- timestamp syntax;
- start < end;
- nondecreasing event order;
- no clearly accidental multi-minute persistence;
- no unexpected empty captions;
- reasonable correspondence between extracted source events and output entries.

Report corrections transparently.
