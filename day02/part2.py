from __future__ import annotations

import os
from enum import Enum

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


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
        }
        return mapping[char]

    @property
    def score(self) -> int:
        return list(ShapeEnum).index(self) + 1

    def score_for(self, outcome: str) -> int:
        if outcome == "Y":
            return self.score
        len_figures = len(ShapeEnum)
        if outcome == "X":
            return (self.score - 1) or list(ShapeEnum)[-1].score
        if outcome == "Z":
            return ((self.score + 1) % len_figures) or len_figures


def compute(s: str) -> int:
    total_score = 0
    for line in s.splitlines():
        enemy, outcome = line.split()
        enemy_shape = ShapeEnum.from_char(enemy)
        total_score += enemy_shape.score_for(outcome)
        outcome_scores = {
            "X": 0,
            "Y": 3,
            "Z": 6,
        }
        total_score += outcome_scores[outcome]
    return total_score


INPUT_S = '''\
A Y
B X
C Z
B Z
A X
'''
EXPECTED = 24


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
