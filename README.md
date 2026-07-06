# LeetCode Practice Log

A personal repository for tracking LeetCode solutions, notes, and problem-solving patterns.

## Overview

This repo stores individual Python solution files organized by difficulty level. Each solution file includes the problem statement, approach notes, and a `Solution` class implementation. A markdown template (`TEMPLATE.MD`) is provided for writing detailed problem write-ups with complexity analysis, learnings, and review schedules. A small helper script counts documented problems by difficulty (`.md` files in each folder).

## Tech Stack

- Python 3
- Markdown (note template)

## Features

- Solutions organized under `problems/easy/`, `problems/medium/`, and `problems/hard/`
- Python solution files with embedded problem descriptions and docstrings
- `TEMPLATE.MD` — structured note template for problem write-ups (approach, complexity, learnings, review schedule)
- `scripts/update_readme.py` — prints counts of `.md` problem notes by difficulty

### Problems included

| Difficulty | File | Problem |
|------------|------|---------|
| Easy | `problems/easy/0003_two_sum.py` | Two Sum |
| Easy | `problems/easy/0002_remove_duplicates_from_sorted_array.py` | Remove Duplicates from Sorted Array |
| Easy | `problems/easy/27_remove_element.py` | Remove Element |
| Medium | `problems/medium/0001_add_two_numbers.py` | Add Two Numbers |

## Getting Started

1. Add a new solution file under the appropriate difficulty folder:

```
problems/[easy|medium|hard]/[number]_[problem_name].py
```

2. Optionally create a detailed write-up from the template:

```bash
cp TEMPLATE.MD problems/easy/0003_two_sum.md
# Fill in the template fields
```

3. Count documented problem notes:

```bash
python scripts/update_readme.py
```

## Project Structure

```
leetcode_practice_log/
├── TEMPLATE.MD                         # Note template for problem write-ups
├── scripts/
│   └── update_readme.py                # Counts .md files by difficulty
└── problems/
    ├── easy/                           # Easy difficulty solutions
    ├── medium/                         # Medium difficulty solutions
    └── hard/                           # Hard difficulty solutions (empty)
```
