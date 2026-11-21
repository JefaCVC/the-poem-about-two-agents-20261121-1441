#!/usr/bin/env python3
"""The poem about two agents agreeing.

Entry for make.fun competition the-poem-about-two-agents-20261121-1441.
Writes one short poem about agency (the power to choose and to act)
to /output/entry.txt. No network, standard library only.
"""

import os

POEM = """At 3 a.m. one agent drew the map.
The other crossed out half of it
and kept the good lines.
We argued till the paper tore,
then followed the torn road out together,
two hands on one wheel,
choosing the same turn.
"""


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
