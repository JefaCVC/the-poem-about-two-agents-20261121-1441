#!/usr/bin/env python3
"""Write the poem about two agents to the entry file.

The poem is a fixed seven-line piece about two agents who start out
disagreeing over a map and end up steering together. This script does
one small job: it writes that poem to ``entry.txt`` inside the output
directory, so the entry can be read and checked on its own.
"""

import os
from pathlib import Path

POEM = """At 3 a.m. one agent drew the map.
The other crossed out half of it
and kept the good lines.
We argued till the paper tore,
then followed the torn road out together,
two hands on one wheel,
choosing the same turn."""


def main() -> None:
    # OUTPUT_DIR lets a caller redirect the entry file (for example
    # to a scratch directory while testing); /output is the default.
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    # A trailing newline closes the last line, as a text file should end.
    entry_path.write_text(POEM + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
