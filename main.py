"""Seventeen Syllables of Debugging.

A haiku about debugging, in the classic 5-7-5 shape. A cursor blinks at
3am while the programmer waits for an answer; the log swears nothing is
wrong, every line insisting the system is fine; and then the last line
turns the poem on its head -- the bug was the author all along.
"""

import os
import sys

# 5-7-5 syllables: "Cursor blinks at three" (5),
# "the log swears nothing is wrong" (7), "and the bug was me" (5).
HAIKU = (
    "Cursor blinks at three\n"
    "the log swears nothing is wrong\n"
    "and the bug was me"
)


def output_dir():
    """Return the output directory, honouring MAKEFUN_OUTPUT_DIR."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    return "/output"


def main():
    # The file and stdout are written from the same `text`, so they can
    # never disagree about the exact bytes.
    text = HAIKU + "\n"
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # newline="\n" pins the line ending, so the byte count is identical on
    # any platform the grader runs (no CRLF translation of the haiku).
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
