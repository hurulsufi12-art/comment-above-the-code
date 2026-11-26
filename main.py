"""The Comment Above the Code.

Writes one line — the comment a developer left above fragile production
code — to /output/entry.txt.

The line is a fixed string. Before anything is written, the line is run
through a table of gate checks taken from the bounty rules (UTF-8 text,
1 to 200 characters, not only whitespace, a single line, no control
characters). If any check fails, the program reports the first failure
and exits non-zero without writing a file.
"""

import os
import sys

FINAL_TEXT = "// This only works because two bugs cancel each other out. One of them is load-bearing."

DEFAULT_OUTPUT = "/output/entry.txt"
MAX_CHARS = 200


def _has_minimum_length(line):
    return len(line) >= 1


def _fits_character_cap(line):
    return len(line) <= MAX_CHARS


def _is_not_blank(line):
    return bool(line.strip())


def _is_single_line(line):
    return line.splitlines() == [line]


def _has_no_control_characters(line):
    return not any(ord(ch) < 32 for ch in line)


# Table-driven gate: each row is (label, predicate). main() walks the
# table in order and stops at the first failing row.
RULES = [
    ("at least 1 character", _has_minimum_length),
    ("at most 200 characters", _fits_character_cap),
    ("not whitespace-only", _is_not_blank),
    ("exactly one line", _is_single_line),
    ("no control characters", _has_no_control_characters),
]


def validate_text(line):
    """Return a list of the labels of every gate rule the line breaks."""
    return [label for label, check in RULES if not check(line)]


def resolve_output_path():
    """Grader path by default; tests may redirect it with ENTRY_OUTPUT."""
    return os.environ.get("ENTRY_OUTPUT", DEFAULT_OUTPUT)


def main():
    failures = validate_text(FINAL_TEXT)
    if failures:
        print(f"gate failed: {failures[0]}", file=sys.stderr)
        return 1
    target = resolve_output_path()
    parent = os.path.dirname(target)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(target, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(FINAL_TEXT + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
