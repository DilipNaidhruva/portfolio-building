# Simple Line Editor (Minimal Edition) — C

Built for: Portfolio Building Studio Course — Coding Competition (3rd Semester)

## Team
- Member 1: _<M.Sam Priyan>_
- Member 2: _<DilipNaidhruva>_
- Member 3: _<Shrisam_Ambig>_


## Features Implemented

**Core (all 4 available — required minimum was 2-3):**
- Insert a line (`INS`)
- Delete a line (`DEL`)
- Display the document (`SHOW`)
- Save / load a file (`SAVE`, `LOAD`)

**Bonus:**
- Search (`FIND`) — find and report which line(s) contain a word or phrase
- Find & replace (`REPLACE`) — replace a word/phrase across the whole document
- Undo (`UNDO`) — reverse the most recent change (single-level)
- Line count / word count (`STATS`) — also reports total character count

**Extras beyond the brief:**
- `EDIT` — overwrite an entire line's content directly
- `CLEAR` — empty the whole document in one step
- `UPPER` / `LOWER` — convert the whole document's case
- Case-insensitive command names (`ins`, `INS`, `Ins` all work)

See [`HELP.md`](HELP.md) for full command documentation with examples.

## Data Structure

The document is held as a fixed-size 2D character array:

```c
typedef struct { char lines[MAX_L][MAX_C]; int count; } Document;
```

up to `MAX_L = 500` lines of up to `MAX_C = 255` characters each, plus a
`count` of lines currently in use. This gives O(1) access to any line by
number (the editor's most frequent operation) and keeps the code simple
— no manual memory management, no pointers to track. The trade-off is a
hard ceiling on document size and per-line length, and a larger memory
footprint reserved up front regardless of how much is actually used.

Undo is implemented as a single extra `Document` struct (`undo_stack`).
Because `Document` is a plain fixed-size struct, `undo_stack = doc;`
performs a full copy in one line — no manual loop needed. This gives a
**single-level** undo (it reverses only the most recent change) covering
every mutating command: `INS`, `DEL`, `EDIT`, `LOAD`, `REPLACE`, `CLEAR`,
`UPPER`, and `LOWER`.

## How to Compile

Requires `gcc` and a C standard library. From the project root:

```bash
gcc -Wall -Wextra -o editor editor.c
```

## How to Run

```bash
./editor
```

Then type `HELP` inside the editor for the command list, or see `HELP.md`.

### Quick example session

```
$ ./editor
=========================================
 Simple Line Editor (Minimal Edition)
=========================================
Type HELP for available commands.

editor> INS 1 The Quick Brown Fox
Inserted line 1.
editor> INS 2 jumps over the lazy dog
Inserted line 2.
editor> SHOW
--- DOCUMENT START ---
  1 | The Quick Brown Fox
  2 | jumps over the lazy dog
--- DOCUMENT END ---
editor> FIND Brown Fox
Line   1: The Quick Brown Fox
Found 1 match(es).
editor> REPLACE the THE
Replaced 1 occurrence(s).
editor> STATS
Lines: 2 | Words: 9 | Chars: 42
editor> SAVE mydoc.txt
Saved to mydoc.txt.
editor> EXIT
```

## Project Structure

```
.
├── editor.c     # full implementation
├── HELP.md      # command reference with usage examples
└── README.md    # this file
```

## Note on Paper Design

The competition rubric asks for a hand-written paper design (data
structure choice, command set, function outline) submitted as a photo
or scan, completed **before** any code was typed. That's a separate,
physical deliverable for your team — this README and HELP.md don't
replace it.
