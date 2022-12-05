from __future__ import annotations

import os
from typing import NamedTuple

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


class Command(NamedTuple):
    element: int
    from_: int
    to: int


def compute(s: str) -> str:
    stacks, moves, *_ = s.split('\n\n')
    *stack_lines, indexes = stacks.splitlines()
    layers_len = int(indexes.strip().split()[-1])
    layers = [[] for _ in range(layers_len)]
    for line in stacks.splitlines()[:-1]:
        for i, char in enumerate(line):
            if char not in " []" and indexes[i].strip():
                layer_index = int(indexes[i]) - 1
                layers[layer_index].append(char)
    layers = [list(reversed(layer)) for layer in layers]

    for line in moves.splitlines():
        parts = line.split()
        command = Command(element=int(parts[1]) * -1, from_=int(parts[3]) - 1, to=int(parts[5]) - 1)
        elements = layers[command.from_][command.element:]
        layers[command.from_] = layers[command.from_][:command.element]
        layers[command.to].extend(elements)

    return "".join([el[-1] for el in layers if el])


INPUT_S = '''\
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
'''
EXPECTED = "MCD"


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
