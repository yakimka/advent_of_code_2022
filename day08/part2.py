from __future__ import annotations

import os
from typing import Iterable, Sequence

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    matrix = []
    for line in s.splitlines():
        matrix.append([int(c) for c in line.strip()])

    def compute_scores_in_rows_to_left(rows: Iterable[Sequence[int]]) -> list[list[int]]:
        result = []
        for row in rows:
            stack = []
            scores = []
            for i, val in enumerate(row):
                while stack and val > row[stack[-1]]:
                    stack.pop()

                last_index = stack[-1] if stack else 0
                scores.append(i - last_index)
                stack.append(i)
            result.append(scores)
        return result

    visible_left = compute_scores_in_rows_to_left(matrix)
    visible_right = compute_scores_in_rows_to_left([row[::-1] for row in matrix])
    visible_up = compute_scores_in_rows_to_left(zip(*matrix))
    visible_down = compute_scores_in_rows_to_left([row[::-1] for row in zip(*matrix)])

    max_score = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            score = (
                    visible_left[i][j] *
                    visible_right[i][(j + 1) * -1] *
                    visible_up[j][i] *
                    visible_down[j][(i + 1) * -1]
            )
            max_score = max(max_score, score)
    return max_score


INPUT_S = '''\
30373
25512
65332
33549
35390
'''
EXPECTED = 8


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
