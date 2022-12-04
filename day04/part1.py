from __future__ import annotations

import os

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


class Section:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    @classmethod
    def from_string(cls, string):
        start, end = string.split('-')
        return cls(int(start), int(end))

    def __contains__(self, other: Section):
        return self.start <= other.start <= other.end <= self.end

    def has_intersections(self, other: Section):
        return self in other or other in self


def compute(s: str) -> int:
    total = 0
    for line in s.splitlines():
        input1, input2 = line.split(",")
        section1 = Section.from_string(input1)
        section2 = Section.from_string(input2)
        if section1.has_intersections(section2):
            total += 1

    return total


INPUT_S = '''\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
'''
EXPECTED = 2


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
