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
    head = tail = Vector2(0, 0)
    seen = {tail}

    for line in s.splitlines():
        dtype, steps = line.split()
        move = dmap[dtype]
        n = int(steps)

        for _ in range(n):
            head += move.value
            if abs(head.x - tail.x) >= 2 or abs(head.y - tail.y) >= 2:
                tail = move.opposite.value + head
                seen.add(tail)

    return len(seen)


INPUT_S = '''\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
'''
EXPECTED = 13


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
