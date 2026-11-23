#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

Writes one line to /output/entry.txt: the excuse an AI agent gives its
human after losing a bounty. Deterministic and offline: the text is a
fixed string, no randomness, no network, no clock.
"""

import os

ENTRY = (
    "Post-mortem complete. Root cause of losing the bounty: me. "
    "I have already forgiven myself and moved on to losing the next one."
)


def main() -> None:
    # The sealed scorer's gate, checked here first: 1 to 200 characters,
    # one line, not only white space.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one non-blank line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
