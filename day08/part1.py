from __future__ import annotations

import os
from typing import Iterable

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    matrix = []
    for line in s.splitlines():
        matrix.append([int(c) for c in line.strip()])

    def compute_visible_in_rows_to_left(rows: Iterable[Iterable[int]]) -> list[list[int]]:
        result = []
        for row in rows:
            max_val = -1
            new_row = []
            for val in row:
                if val > max_val:
                    new_row.append(True)
                    max_val = val
                    continue
                new_row.append(False)
            result.append(new_row)

        return result

    visible_left = compute_visible_in_rows_to_left(matrix)
    visible_right = compute_visible_in_rows_to_left([row[::-1] for row in matrix])
    visible_up = compute_visible_in_rows_to_left(zip(*matrix))
    visible_down = compute_visible_in_rows_to_left([row[::-1] for row in zip(*matrix)])

    total = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            total += int(
                    visible_left[i][j] or
                    visible_right[i][(j + 1) * -1] or
                    visible_up[j][i] or
                    visible_down[j][(i + 1) * -1]
            )
    return total


INPUT_S = '''\
30373
25512
65332
33549
35390
'''
EXPECTED = 21


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
