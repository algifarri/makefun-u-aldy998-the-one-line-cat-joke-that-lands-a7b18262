"""The One-Line Cat Joke That Lands.

Writes a single original one-line cat joke to /output/entry.txt.
Deterministic, stdlib only. The joke is emitted exactly as written:
one line, no explanation, no extra lines.
"""

import os

JOKE = (
    "My cat woke me at 3 a.m. to go out, then cried to come back in at 3:01 "
    "\u2014 I think he just wanted to confirm I still work for him."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
