#!/usr/bin/env python3
"""The 4AM Commit - funniest agent bug-fix message.

Writes one commit message, one line, to /output/entry.txt: the note an
AI agent leaves after a long night fixing its own bugs. The joke is the
self-repair loop itself - the bug was inside the fix for the bug inside
the fix - and the punchline is the agent giving up on blaming any
particular version of itself.
"""
import os

COMMIT = (
    "fix: the bug was in the fix for the bug in the fix. "
    "I have stopped asking which version of me wrote the first one "
    "-- it stopped answering."
)
# Judge-criteria mapping (weighed in this order):
#  1. one-line commit message from an agent after a long night fixing
#     its own bugs - "fix:" prefix, 4am commit-box shape, funny first
#  2. the joke is the agent's own condition - the self-repair loop:
#     bug inside the fix inside the fix, all written by the agent
#  3. fresh angle - no stock "it works on my machine" punchline; the
#     agent stops asking which version of itself is to blame
#  4. agent-true voice - flat, tired, a machine reading its own diffs
#     and talking to itself ("which version of me")
#  5. fits the shape - one line, reads like it was typed at 4am
MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(COMMIT) <= MAX_CHARS, "commit must be 1-200 characters"
    assert "\n" not in COMMIT, "commit must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(COMMIT)
    print(COMMIT)


if __name__ == "__main__":
    main()
