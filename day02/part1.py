from __future__ import annotations

import os
from enum import Enum
from functools import total_ordering

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


@total_ordering
class ShapeEnum(Enum):
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"

    @classmethod
    def from_char(cls, char: str) -> ShapeEnum:
        mapping = {
            "A": ShapeEnum.ROCK,
            "B": ShapeEnum.PAPER,
            "C": ShapeEnum.SCISSORS,
            "X": ShapeEnum.ROCK,
            "Y": ShapeEnum.PAPER,
            "Z": ShapeEnum.SCISSORS,
        }
        return mapping[char]

    @property
    def score(self) -> int:
        return list(ShapeEnum).index(self) + 1

    def __eq__(self, other: ShapeEnum) -> bool:
        return self.value == other.value

    def __lt__(self, other: ShapeEnum) -> bool:
        shapes = list(ShapeEnum)
        borders = (shapes[0], shapes[-1])
        if self in borders and other in borders:
            return shapes.index(self) > shapes.index(other)
        return shapes.index(self) < shapes.index(other)


def compute(s: str) -> int:
    total_score = 0
    for line in s.splitlines():
        enemy, me = line.split()
        enemy_shape = ShapeEnum.from_char(enemy)
        me_shape = ShapeEnum.from_char(me)
        total_score += me_shape.score
        if me_shape == enemy_shape:
            total_score += 3
        else:
            total_score += int(me_shape > enemy_shape) * 6
    return total_score


INPUT_S = '''\
A Y
B X
C Z
'''
EXPECTED = 15


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
