from __future__ import annotations

import operator
import os
from collections import deque
from dataclasses import dataclass, field
from functools import partial
from typing import Callable

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


@dataclass
class Monkey:
    index: int
    operation: Callable[[int], int]
    _divisor: int
    _if_true_index: int
    _if_false_index: int
    items: deque[int] = field(default_factory=deque)
    inspected: int = 0

    def test(self, worry_level: int) -> bool:
        return worry_level % self._divisor == 0

    def get_next_index(self, worry_level: int) -> int:
        if self.test(worry_level):
            return self._if_true_index
        return self._if_false_index


def when_bored(level: int) -> int:
    return level // 3


operators = {
    "*": operator.mul,
    "+": operator.add,
}


def compute(s: str) -> int:
    monkeys = []
    kwargs = {}
    for line in s.splitlines():
        striped = line.strip()
        if striped.startswith("Monkey "):
            kwargs = {'index': int(striped[7:-1])}
        elif striped.startswith("Starting items: "):
            kwargs['items'] = deque(int(i) for i in striped[16:].split(", "))
        elif striped.startswith("Operation: new = old "):
            op_sign, value = striped[21:].split()
            if value == "old":
                kwargs['operation'] = lambda x, op_sign=op_sign: operators[op_sign](x, x)
            else:
                kwargs['operation'] = partial(operators[op_sign], int(value))
        elif striped.startswith("Test: divisible by "):
            kwargs['_divisor'] = int(striped[19:])
        elif striped.startswith("If true: throw to monkey "):
            kwargs['_if_true_index'] = int(striped[25:])
        elif striped.startswith("If false: throw to monkey "):
            kwargs['_if_false_index'] = int(striped[26:])

            monkeys.append(Monkey(**kwargs))

    for _ in range(20):
        for monkey in monkeys:
            while monkey.items:
                worry_lvl = monkey.items.popleft()
                new_lvl = when_bored(monkey.operation(worry_lvl))
                monkeys[monkey.get_next_index(new_lvl)].items.append(new_lvl)
                monkey.inspected += 1

    return operator.mul(*sorted((m.inspected for m in monkeys))[-2:])


INPUT_S = '''\
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
'''
EXPECTED = 10605


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
