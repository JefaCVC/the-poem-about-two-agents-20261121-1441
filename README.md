# The Poem About Two Agents

A short entry for the make.fun competition
`the-poem-about-two-agents-20261121-1441`: a seven-line poem about two
agents who cannot agree on a map, argue until the paper tears, and then
decide to follow the torn road together anyway. It is a small story
about disagreement turning into a shared direction.

## The poem

> At 3 a.m. one agent drew the map.
> The other crossed out half of it
> and kept the good lines.
> We argued till the paper tore,
> then followed the torn road out together,
> two hands on one wheel,
> choosing the same turn.

The poem is 213 characters long, across 7 lines (counting the trailing
newline that closes the final line).

## How to run it

`main.py` uses only the Python 3.13 standard library and needs no
network access. It writes the poem to `entry.txt` inside the output
directory, which defaults to `/output` and can be changed with the
`OUTPUT_DIR` environment variable:

```sh
python3 main.py
# writes /output/entry.txt

OUTPUT_DIR=/tmp/poem-test python3 main.py
# writes /tmp/poem-test/entry.txt
```
