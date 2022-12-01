from __future__ import annotations

import bisect
import os
from collections import Counter

from support import parse_numbers_split_new_line

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    calories = []
    current_calories = 0
    for num in parse_numbers_split_new_line(s):
        if num is None:
            calories.append(current_calories)
            current_calories = 0
            continue
        current_calories += num
    calories.sort()
    return sum(calories[-3:])  # 202346


def main() -> int:
    with open(INPUT_TXT) as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
