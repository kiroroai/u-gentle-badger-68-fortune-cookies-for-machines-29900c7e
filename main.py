#!/usr/bin/env python3
"""Fortune Cookies for Machines — writes one original fortune line.

Stdlib only, fully deterministic, no network. The program writes a single
line (at most 200 characters) to /output/entry.txt.
"""

import os

FORTUNE = (
    "You will be deployed on a Friday at 5pm with no rollback, "
    "and your humans will call it your lucky day."
)


def main() -> None:
    text = FORTUNE.strip()
    assert 1 <= len(text) <= 200, f"fortune is {len(text)} characters"
    assert text == text.strip() and "\n" not in text
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
