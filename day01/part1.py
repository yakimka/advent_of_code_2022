from __future__ import annotations

import os

from support import parse_numbers_split_new_line

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    max_calories = 0
    current_calories = 0
    for num in parse_numbers_split_new_line(s):
        if num is None:
            max_calories = max(max_calories, current_calories)
            current_calories = 0
            continue
        current_calories += num
    return max_calories  # 69501


def main() -> int:
    with open(INPUT_TXT) as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
