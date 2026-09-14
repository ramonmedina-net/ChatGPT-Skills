# Task Instructions

## Preparation task

Inputs:
- local source media file;
- optional explicit subtitle track ID;
- optional output directory.

Outputs:
- native bitmap subtitle asset(s);
- task manifest;
- preparation report.

### Normal procedure

1. Confirm execution approval unless already explicitly supplied.
2. Run the fresh PowerShell preparation script.
3. Review detected tracks.
4. If exactly one relevant English bitmap track is present, extract it.
5. If multiple materially different English bitmap tracks are present and the user has not identified one, stop after inspection and ask which track should be used.
6. Preserve native files without transcoding.

## Transcription/conversion task

After preparation:
1. decode/render the bitmap subtitle events using an appropriate local workflow;
2. transcribe event text;
3. preserve event timing;
4. produce SRT;
5. validate structure/timing;
6. flag uncertain events.

## No silent assumptions

Do not assume:
- every English subtitle track is bitmap;
- the first English track is the desired track;
- an absent cue means silence;
- missing end times should extend to the next event;
- a source file may be overwritten.

## Completion report

State:
- source title/file;
- selected track;
- codec/language;
- extracted native files;
- output SRT path;
- caption/event count;
- validation issues/corrections;
- unresolved uncertainties.
