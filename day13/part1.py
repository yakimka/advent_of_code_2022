from __future__ import annotations

import os
from itertools import zip_longest

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def to_list(val: int | list):
    if isinstance(val, int):
        return [val]
    return val


def compute(s: str) -> int:
    right_orders = []
    for i, line in enumerate(s.split("\n\n"), start=1):
        l_str, r_str = line.strip().split("\n")
        if compare(eval(l_str), eval(r_str)) <= 0:
            right_orders.append(i)

    return sum(right_orders)


def compare(left: list, right: list) -> int:
    for l, r in zip_longest(left, right, fillvalue=None):
        if l is None:
            return -1
        elif r is None:
            return 1

        if any(isinstance(x, list) for x in (l, r)):
            res = compare(to_list(l), to_list(r))
            if res != 0:
                return res
        else:
            res = l - r
            if res != 0:
                return res

    return 0


INPUT_S = '''\
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
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
