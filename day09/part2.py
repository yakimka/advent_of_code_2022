from __future__ import annotations

import os
from enum import Enum

import pytest

from support import Vector2

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


class Direction(Enum):
    UP = Vector2(0, -1)
    RIGHT = Vector2(1, 0)
    DOWN = Vector2(0, 1)
    LEFT = Vector2(-1, 0)

    @property
    def opposite(self) -> Vector2:
        vals = tuple(type(self).__members__.values())
        return vals[(vals.index(self) + 2) % len(vals)]


dmap = {
    "U": Direction.UP,
    "R": Direction.RIGHT,
    "D": Direction.DOWN,
    "L": Direction.LEFT,
}


def compute(s: str) -> int:
    knots = [Vector2(0, 0) for _ in range(10)]
    seen = {knots[-1]}

    for line in s.splitlines():
        dtype, steps = line.split()
        move = dmap[dtype]
        n = int(steps)

        for _ in range(n):
            knots[0] += move.value

            prev = knots[0]
            for i in range(1, len(knots)):
                curr = knots[i]
                diff_abs = abs(prev - curr)
                sum_floordived = (prev + curr) // 2
                if diff_abs == (2, 2):
                    knots[i] = sum_floordived
                elif diff_abs.x == 2:
                    knots[i] = Vector2(sum_floordived.x, prev.y)
                elif diff_abs.y == 2:
                    knots[i] = Vector2(prev.x, sum_floordived.y)
                prev = knots[i]
            seen.add(knots[-1])

    return len(seen)


INPUT_S = '''\
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
'''
EXPECTED = 36


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
