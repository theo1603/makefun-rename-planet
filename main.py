#!/usr/bin/env python3
"""Write one funny new name for a planet to /output/entry.txt.

The line renames Saturn "The Prenup": its rings are the wedding ring
it already wears, and the joke is that four billion years into the
engagement it still won't set a date. The why leans on Saturn's own
trait — the rings, which no other planet wears like this — so the name
would not fit any other planet, and the laugh comes from the idea
(ring -> engagement stalled forever), not from a pun on "Saturn".

Revision: the first draft ended "after four billion years it still
hasn't set a wedding date." It was revised to "four billion years
into the engagement it still won't set a date": "engagement" names
the ring's promise instead of repeating "wedding", and "won't" makes
Saturn stubborn rather than merely late, so the punchline lands on
the planet's refusal. The line runs 140 chars, five more than the
draft, but every word now earns its place.
"""

from pathlib import Path

TEXT = (
    "Rename Saturn 'The Prenup' — the only planet already wearing "
    "the ring, and four billion years into the engagement it still "
    "won't set a date."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
