<#
.SYNOPSIS
  Prepare native bitmap subtitle tracks from a local media file.

.DESCRIPTION
  - Never modifies the source media.
  - Prefers MKVToolNix for MKV inspection/extraction.
  - Detects English PGS/VobSub subtitle tracks.
  - Extracts PGS as .sup and VobSub as .idx/.sub.
  - Writes task_manifest.json and PREPARATION_REPORT.md.
  - Performs no network downloads or installations.

.PARAMETER InputMedia
  Path to the source media file.

.PARAMETER OutputDir
  Optional output directory. Defaults to a sibling folder named
  <source-basename>_bitmap_subtitles.

.PARAMETER TrackId
  Optional MKVToolNix track ID to extract. If omitted, all English bitmap
  subtitle tracks are listed and extraction proceeds automatically only
  when exactly one matching track exists.

.PARAMETER Overwrite
  Allow overwriting extracted outputs in the destination directory.
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory=$true)]
    [string]$InputMedia,

    [string]$OutputDir,

    [int]$TrackId = -1,

    [switch]$Overwrite
)

$ErrorActionPreference = "Stop"

function Find-Executable {
    param(
        [Parameter(Mandatory=$true)][string]$Name,
        [string[]]$CommonPaths = @()
    )

    $cmd = Get-Command $Name -ErrorAction SilentlyContinue
    if ($cmd) { return $cmd.Source }

    foreach ($p in $CommonPaths) {
        if ($p -and (Test-Path -LiteralPath $p -PathType Leaf)) {
            return (Resolve-Path -LiteralPath $p).Path
        }
    }

    return $null
}

function Get-FileSha256 {
    param([string]$Path)
    return (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash.ToLowerInvariant()
}

$source = (Resolve-Path -LiteralPath $InputMedia).Path
$sourceItem = Get-Item -LiteralPath $source

if (-not $OutputDir) {
    $parent = Split-Path -Parent $source
    $base = [IO.Path]::GetFileNameWithoutExtension($source)
    $OutputDir = Join-Path $parent ($base + "_bitmap_subtitles")
}
$out = [IO.Path]::GetFullPath($OutputDir)

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$possibleToolRoot = Join-Path (Split-Path -Parent $scriptDir) "tools"

$mkvmerge = Find-Executable "mkvmerge.exe" @(
    "$env:ProgramFiles\MKVToolNix\mkvmerge.exe",
    "${env:ProgramFiles(x86)}\MKVToolNix\mkvmerge.exe",
    (Join-Path $possibleToolRoot "MKVToolNix\mkvmerge.exe")
)

$mkvextract = Find-Executable "mkvextract.exe" @(
    "$env:ProgramFiles\MKVToolNix\mkvextract.exe",
    "${env:ProgramFiles(x86)}\MKVToolNix\mkvextract.exe",
    (Join-Path $possibleToolRoot "MKVToolNix\mkvextract.exe")
)

$ffprobe = Find-Executable "ffprobe.exe" @(
    (Join-Path $possibleToolRoot "ffmpeg\bin\ffprobe.exe")
)

$subtitleEdit = Find-Executable "SubtitleEdit.exe" @(
    "$env:ProgramFiles\Subtitle Edit\SubtitleEdit.exe",
    "${env:ProgramFiles(x86)}\Subtitle Edit\SubtitleEdit.exe",
    (Join-Path $possibleToolRoot "SubtitleEdit\SubtitleEdit.exe")
)

Write-Host ""
Write-Host "Bitmap Subtitle Preparation"
Write-Host "==========================="
Write-Host "Source: $source"
Write-Host "Output: $out"
Write-Host ""
Write-Host "Detected tools:"
Write-Host ("  mkvmerge   : " + $(if ($mkvmerge) { $mkvmerge } else { "MISSING" }))
Write-Host ("  mkvextract : " + $(if ($mkvextract) { $mkvextract } else { "MISSING" }))
Write-Host ("  ffprobe    : " + $(if ($ffprobe) { $ffprobe } else { "not found (optional)" }))
Write-Host ("  SubtitleEdit: " + $(if ($subtitleEdit) { $subtitleEdit } else { "not found (optional)" }))
Write-Host ""

$ext = [IO.Path]::GetExtension($source).ToLowerInvariant()

if ($ext -ne ".mkv") {
    Write-Host "This portable preparation script currently performs native extraction for MKV sources."
    if ($ffprobe) {
        Write-Host "ffprobe is available for inspection, but this script will not guess a safe native extraction mapping for this container."
    }
    throw "Unsupported source container for automatic extraction: $ext. Use an MKV source or extend the workflow explicitly."
}

if (-not $mkvmerge -or -not $mkvextract) {
    throw "MKVToolNix is required for the native MKV bitmap-subtitle workflow. Missing: $(
        @(
            if (-not $mkvmerge) { 'mkvmerge.exe' }
            if (-not $mkvextract) { 'mkvextract.exe' }
        ) -join ', '
    )"
}

$probeJson = & $mkvmerge -J -- $source
if ($LASTEXITCODE -ne 0) {
    throw "mkvmerge inspection failed with exit code $LASTEXITCODE."
}
$info = $probeJson | ConvertFrom-Json

$bitmapTracks = @()

foreach ($t in $info.tracks) {
    if ($t.type -ne "subtitles") { continue }

    $codec = [string]$t.codec
    $codecId = [string]$t.properties.codec_id
    $lang = [string]$t.properties.language
    $ietf = [string]$t.properties.language_ietf
    $name = [string]$t.properties.track_name

    $isPgs = ($codec -match "PGS|HDMV") -or ($codecId -match "S_HDMV/PGS")
    $isVob = ($codec -match "VobSub|VOBSUB") -or ($codecId -match "S_VOBSUB")
    if (-not ($isPgs -or $isVob)) { continue }

    $isEnglish = ($lang -match "^(eng|en)$") -or ($ietf -match "^en(?:-|$)")
    if (-not $isEnglish) { continue }

    $bitmapTracks += [pscustomobject]@{
        id = [int]$t.id
        codec = $codec
        codec_id = $codecId
        language = $lang
        language_ietf = $ietf
        name = $name
        default_track = [bool]$t.properties.default_track
        forced_track = [bool]$t.properties.forced_track
        kind = $(if ($isPgs) { "PGS" } else { "VobSub" })
    }
}

if ($bitmapTracks.Count -eq 0) {
    Write-Host "No English PGS/VobSub subtitle tracks were found."
    Write-Host "Available subtitle tracks:"
    $info.tracks | Where-Object type -eq "subtitles" | ForEach-Object {
        Write-Host ("  ID {0}: codec={1}; language={2}; name={3}" -f $_.id, $_.codec, $_.properties.language, $_.properties.track_name)
    }
    throw "No matching English bitmap subtitle track found."
}

Write-Host "English bitmap subtitle tracks:"
$bitmapTracks | Format-Table id,kind,language,language_ietf,name,default_track,forced_track -AutoSize

$selected = @()
if ($TrackId -ge 0) {
    $selected = @($bitmapTracks | Where-Object id -eq $TrackId)
    if ($selected.Count -ne 1) {
        throw "TrackId $TrackId is not one of the detected English bitmap subtitle tracks."
    }
} elseif ($bitmapTracks.Count -eq 1) {
    $selected = @($bitmapTracks[0])
} else {
    Write-Host ""
    Write-Host "Multiple English bitmap tracks exist. No extraction was performed."
    Write-Host "Re-run with -TrackId <id> after choosing the desired track."
    exit 3
}

if (-not (Test-Path -LiteralPath $out)) {
    New-Item -ItemType Directory -Path $out | Out-Null
}

$extracted = @()

foreach ($t in $selected) {
    $safeName = if ($t.name) {
        ($t.name -replace '[^\w\-. ]','_').Trim()
    } else {
        "track"
    }
    if (-not $safeName) { $safeName = "track" }

    if ($t.kind -eq "PGS") {
        $target = Join-Path $out ("subtitle_{0}_{1}.sup" -f $t.id, $safeName)
    } else {
        $target = Join-Path $out ("subtitle_{0}_{1}.idx" -f $t.id, $safeName)
    }

    if ((Test-Path -LiteralPath $target) -and -not $Overwrite) {
        throw "Output already exists: $target. Re-run with -Overwrite only if replacement is intended."
    }

    Write-Host "Extracting track $($t.id) -> $target"
    & $mkvextract tracks -- $source "$($t.id):$target"
    if ($LASTEXITCODE -ne 0) {
        throw "mkvextract failed for track $($t.id) with exit code $LASTEXITCODE."
    }

    $files = @()
    if ($t.kind -eq "PGS") {
        $files = @($target)
    } else {
        $subCompanion = [IO.Path]::ChangeExtension($target, ".sub")
        $files = @($target, $subCompanion) | Where-Object { Test-Path -LiteralPath $_ }
    }

    foreach ($f in $files) {
        $fi = Get-Item -LiteralPath $f
        $extracted += [pscustomobject]@{
            track_id = $t.id
            kind = $t.kind
            path = $fi.FullName
            bytes = $fi.Length
            sha256 = Get-FileSha256 $fi.FullName
        }
    }
}

$manifest = [ordered]@{
    skill = "Bitmap Subtitle Transcription / Conversion"
    skill_version = "1.0.0-reconstructed"
    prepared_at = (Get-Date).ToString("o")
    source = [ordered]@{
        path = $source
        bytes = $sourceItem.Length
        last_write_time = $sourceItem.LastWriteTime.ToString("o")
    }
    tools = [ordered]@{
        mkvmerge = $mkvmerge
        mkvextract = $mkvextract
        ffprobe = $ffprobe
        subtitle_edit = $subtitleEdit
    }
    selected_tracks = $selected
    extracted_files = $extracted
}

$manifestPath = Join-Path $out "task_manifest.json"
$manifest | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $manifestPath -Encoding UTF8

$reportPath = Join-Path $out "PREPARATION_REPORT.md"
$report = @"
# Bitmap Subtitle Preparation Report

- Source: `$source`
- Prepared: $($manifest.prepared_at)
- Output directory: `$out`
- Selected track ID(s): $($selected.id -join ", ")
- Selected codec(s): $($selected.kind -join ", ")
- Extracted file count: $($extracted.Count)

## Safety

The source media was read only. Native subtitle tracks were extracted to a separate output directory. No third-party software was downloaded or installed by this script.
"@
Set-Content -LiteralPath $reportPath -Value $report -Encoding UTF8

Write-Host ""
Write-Host "Preparation complete."
Write-Host "Manifest: $manifestPath"
Write-Host "Report  : $reportPath"
Write-Host "Native subtitle asset(s):"
$extracted | ForEach-Object { Write-Host ("  " + $_.path) }
