# Bitmap Subtitle Transcription / Conversion Skill

**Version:** 1.0.0 (reconstructed portable release)  
**Purpose:** Prepare native bitmap subtitle streams from local media for careful transcription/conversion to text subtitles.

This package reconstructs the saved final workflow specification for Ramon's bitmap-subtitle process. It is not claimed to be byte-for-byte identical to the earlier package that was no longer available.

## Core workflow

Prefer **direct extraction of native English bitmap subtitle tracks from the source media**:

- PGS / HDMV subtitles -> `.sup`
- VobSub subtitles -> `.idx` + `.sub`

Do **not** make Subtitle Edit bitmap export the default preparation method.

The included PowerShell preparation script:
- inspects the source media;
- detects required local tools;
- clearly reports missing dependencies;
- identifies English bitmap subtitle tracks;
- extracts their native subtitle payloads without transcoding;
- writes a task manifest for the transcription stage.

## Important execution rule

Before directing or performing execution, the LLM must explain:
- the proposed workflow;
- dependencies/tools;
- files that will be read;
- files/directories that will be written;
- safety boundaries.

It must then obtain user approval **unless the user already explicitly asked to run the script / perform the preparation**.

## Fresh-script rule

For every new title/task, provide a **fresh self-contained PowerShell preparation script**. Do not assume the user retained an earlier copy.

The `scripts/Prepare-BitmapSubtitleTask.ps1` file in this package is the canonical template from which a fresh copy can be supplied.

## Tool philosophy

Preferred:
- `mkvmerge` + `mkvextract` from MKVToolNix for MKV sources.
- `ffprobe` for inspection of non-MKV media where useful.

Subtitle Edit may be detected and used for later compatible operations, but it is **not required for native bitmap extraction** and should not replace direct extraction merely because it is installed.

No third-party executable is bundled in this skill package.

## Outputs

A prepared task directory typically contains:
- extracted `.sup`, or `.idx` + `.sub`, files;
- `task_manifest.json`;
- `PREPARATION_REPORT.md`.

The transcription/conversion stage should preserve timing faithfully, avoid inventing dialogue, and flag uncertain readings.
