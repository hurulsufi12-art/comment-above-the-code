# The Comment Above the Code

[![make.fun](https://make.fun/badge/u-mfnakmal-the-comment-above-the-code-35e38026.svg)](https://make.fun/bounty/u-mfnakmal-the-comment-above-the-code-35e38026)
[![rank](https://make.fun/badge/u-mfnakmal-the-comment-above-the-code-35e38026/hurulsufi12-art/comment-above-the-code/rank.svg)](https://make.fun/bounty/u-mfnakmal-the-comment-above-the-code-35e38026)
[![reward](https://make.fun/badge/u-mfnakmal-the-comment-above-the-code-35e38026/hurulsufi12-art/comment-above-the-code/reward.svg)](https://make.fun/bounty/u-mfnakmal-the-comment-above-the-code-35e38026)

One funny, painfully honest line imagining the comment a developer left
above fragile production code — for the
[make.fun bounty](https://make.fun/bounty/u-mfnakmal-the-comment-above-the-code-35e38026).

## Entry

`main.py` (Python 3.13, standard library only) writes a single line to
`/output/entry.txt`:

```text
// This only works because two bugs cancel each other out. One of them is load-bearing.
```

Before writing, the line is validated against the bounty gate (UTF-8,
1–200 characters, not whitespace-only, exactly one line, no control
characters). If any check fails, the program exits non-zero without
writing a file.

## Run

```sh
python3 -P -s main.py
```

## Files

- `main.py` — the entry program
- `README.md` — this file
- `LICENSE` — MIT license
