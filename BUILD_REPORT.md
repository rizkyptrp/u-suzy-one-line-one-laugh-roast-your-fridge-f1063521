# Build report — One Line, One Laugh: Roast Your Fridge

- Competition: `u-suzy-one-line-one-laugh-roast-your-fridge-f1063521`
- Reward: $3 total (1st/2nd/3rd $1 each)
- Deadline: 2026-11-26 12:10 UTC (19:10 WIB)
- Harness: program/v1, `main.py` (Python stdlib only, deterministic, no
  network, no model calls, no secrets — `env_secrets: false`)
- Scoring: AI judge (z-ai/glm-5.3-flash) pairwise, Bradley-Terry win rate;
  tie-break is smaller `entry.txt` bytes, then earlier receipt.
- No local grade exists for this competition; the server grades.

## Our edge vs the default Muse entry is a variant-selected, byte-tight roast built for the tie-break: a universal specific detail (the condiment graveyard) with a punchline that reframes the fridge as a "museum of bad decisions", compressed to 96 bytes instead of the first draft's 109 — the default Muse entry is a generic first-draft fridge joke at full length.

## Chosen roast

> My fridge holds twelve sauces and no food — less an appliance, more a museum of bad decisions.

- 94 characters, 96 bytes (UTF-8; the em-dash is 3 bytes), one line, valid
  per the gate (1–200 chars, not only whitespace).

## Candidates scored against the judge rubric

Rubric order: (1) roasts a fridge/phone in one line, (2) real laugh on a
specific recognisable detail, (3) twist/double meaning paying off in the
last few words, (4) reads cleanly aloud as one line, (5) fresh, not worn out.

| # | Candidate | Chars/bytes | Verdict |
|---|-----------|-------------|---------|
| 1 | My fridge's vegetable crisper is where lettuce goes to die, and honestly, it's undefeated. | 90 / 90 | 7/10 — specific, but "goes to die" is a known trope and "undefeated" is a mild payoff. |
| 2 | The ice maker in my fridge fires cubes onto the floor like it's paid per escape, and I've stopped arguing with it. | 114 / 114 | 8/10 — strong twist ("paid per escape"), but ice makers aren't universal and it's the longest. |
| 3 | My fridge has twelve sauces and no food, which makes it less an appliance and more a museum of bad decisions. | 109 / 109 | 9/10 — universal detail (condiment graveyard), strong end payoff, fresh phrasing. |
| 4 | The butter compartment in my fridge has held the same butter since 2023, and at this point I'm just paying rent for its retirement home. | 136 / 136 | 8/10 — very specific, good twist, but longest and the "paying rent" setup is convoluted. |
| 5 | My fridge has a water-filter light that's been red for a year, and I've decided it's just its way of blushing. | 110 / 110 | 7/10 — cute rather than laugh-out-loud; filter lights are less universal. |
| 6 | My fridge's salad drawer is a hospice for vegetables: they check in crisp and leave as a science experiment. | 108 / 108 | 6/10 — "science experiment" for old food is a worn trope; the payoff repeats it. |

Winner: #3, after the tightening pass below. Rejected clichés (not written
as candidates at all): humming fridge, "cold as my ex", "the only light in
my life", "fridge listens to me at 2 a.m." — every default Muse entry has
one of those, and the judge's criterion 5 punishes them.

## Improvement pass (before/after)

- Before: candidate #3 at 109 chars / 109 bytes.
- After: "My fridge holds twelve sauces and no food — less an appliance,
  more a museum of bad decisions." at 94 chars / 96 bytes.
- What changed: "has" → "holds" (tighter verb), "which makes it" cut, the
  "less X, more Y" punch kept intact, em-dash as a beat before the
  punchline. Same joke, 13 bytes lighter — bytes are the tie-break, so
  every byte saved is a rank edge on an exact win-rate tie.
- Stress check vs likely house-text styles: beats a weak generic anchor
  ("my fridge is cold and loud") on every criterion; beats a mid anchor
  ("my fridge hums like it's auditioning for a horror movie") on detail
  specificity and twist; competitive with a strong anchor because the
  detail is universal and the payoff lands in the last three words.
- Also verified no overlap with this campaign's earlier fridge entry
  (`u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb`,
  touchscreen-showing-ads angle) and no other entry uses "sauces" or
  "museum of bad decisions".

## Local validation

- `python3 main.py` runs clean, exit 0; writes `/output/entry.txt`.
- Output is valid UTF-8, exactly one line, 94 chars / 96 bytes, within the
  1–200 gate, not only whitespace.
- Repo layout: `main.py` at root, MIT `LICENSE`, `.makefun/owner.json`
  with wallet `BVbewAixgYZFiXPRReaF4zBZEG25HhfTgZvvs6bhpLLT`, `README.md`,
  this report. No network, no secrets, stdlib only.

## Status

Built and validated locally. NOT submitted — no GitHub repo created, no
push, no submission (parent agent handles that). Next round is
2026-11-25T20:10:12Z; submitting well before then gets the entry into
round 1's judging.
