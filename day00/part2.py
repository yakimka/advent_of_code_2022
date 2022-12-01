from __future__ import annotations

import os

import pytest

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
    calories.append(current_calories)
    calories.sort()
    return sum(calories[-3:])  # 202346


INPUT_S = '''\
1000
2000

3000
4000

700

6000
7000
8000
'''
EXPECTED = 31000


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    with open(INPUT_TXT) as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
