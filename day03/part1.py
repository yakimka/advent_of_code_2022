from __future__ import annotations

import os
from functools import lru_cache
from string import ascii_letters

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    total = 0
    for line in s.splitlines():
        median = len(line) // 2
        first_half = set()
        shared = set()
        for i, c in enumerate(line):
            if i < median:
                first_half.add(c)
            else:
                if c in first_half:
                    shared.add(c)
        total += sum(calc_priority(s) for s in shared)

    return total


@lru_cache(maxsize=52)
def calc_priority(c: str) -> int:
    return ascii_letters.index(c) + 1


INPUT_S = '''\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
'''
EXPECTED = 157


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
