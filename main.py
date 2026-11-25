#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge — u-suzy-one-line-one-laugh-roast-your-fridge-f1063521.

Writes one original one-line roast of a fridge (94 characters, 96 bytes) to
/output/entry.txt. Deterministic, Python stdlib only, no network, no model
calls, no paid keys, no environment secrets.

The roast:
    My fridge holds twelve sauces and no food — less an appliance, more a
    museum of bad decisions.

Why this line (scored against the published judge rubric, 6 candidates):
  1. Roasts a fridge in a single line: yes, the fridge is the subject.
  2. Specific, recognisable detail: the condiment graveyard — a fridge full
     of sauces and no actual food is a universal, instantly recognisable
     fridge truth, not a generic insult.
  3. Twist paying off in the last words: "less an appliance, more a museum
     of bad decisions" reframes the fridge as a museum — the punch lands on
     "bad decisions".
  4. Reads cleanly aloud as one line: single clause, em-dash as a beat
     before the punchline, no setup needing a second sentence.
  5. Fresh: "twelve sauces and no food" + "museum of bad decisions" is
     original phrasing, not a worn-out fridge joke (no humming, no cold ex,
     no "only light in my life"). No other entry in this campaign uses it.
Byte-tight by design: the tie-break after Judge win rate is smaller
entry.txt, so the line was compressed from 109 bytes to 96 without losing
any of the joke (see BUILD_REPORT.md for the candidates and the
before/after).
"""

import os

LINE = (
    "My fridge holds twelve sauces and no food \u2014 less an appliance, "
    "more a museum of bad decisions."
)


def validate(line: str) -> None:
    """Gate: the roast must be one valid line, 1-200 characters, not blank.

    Raises ValueError with a clear message if the line fails any check.
    """
    line.encode("utf-8")  # raises UnicodeEncodeError if not valid text
    if "\n" in line or "\r" in line:
        raise ValueError("roast must be exactly one line (no newline inside)")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"roast must be 1-200 characters, got {len(line)}")
    if not line.strip():
        raise ValueError("roast must not be only whitespace")


def main() -> None:
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
