from __future__ import annotations

import os

import pytest

from support import parse_numbers_split_new_line

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    for num in parse_numbers_split_new_line(s):
        pass

    for line in s.splitlines():
        pass

    return 0


INPUT_S = '''\
'''
EXPECTED = 21000


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
