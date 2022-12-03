from __future__ import annotations

import os
from functools import lru_cache
from string import ascii_letters

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    total = 0
    for chunk in chunker(s.splitlines(), 3):
        shared = set(chunk[0]) & set(chunk[1]) & set(chunk[2])
        total += sum(calc_priority(s) for s in shared)

    return total


def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


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
EXPECTED = 70


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
