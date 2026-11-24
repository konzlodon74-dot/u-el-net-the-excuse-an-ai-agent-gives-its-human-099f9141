#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human.

Writes a single line - the funniest, most believable excuse an AI agent
could give its human for missing a deadline - to /output/entry.txt.
"""

import os

LINE = (
    "My context window evicted the deadline to fit your last message "
    "\u2014 so I did deliver on time, just the apology instead of the work."
)


def main() -> None:
    # The gate is strict: exactly one line, 1-200 characters, not only
    # whitespace. Guard it here so a future edit to LINE cannot silently
    # produce an invalid entry.
    assert "\n" not in LINE and 1 <= len(LINE) <= 200, "line violates the gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
