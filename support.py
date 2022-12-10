from __future__ import annotations

from dataclasses import dataclass
from typing import Generator


def parse_numbers_split_new_line(s: str) -> Generator[int | None, None, None]:
    for line in s.splitlines():
        try:
            yield int(line)
        except ValueError:
            yield None


@dataclass(frozen=True)
class Vector2:
    x: int
    y: int

    def __iter__(self):
        return iter((self.x, self.y))

    def __add__(self, other):
        x, y = other
        return type(self)(self.x + x, self.y + y)

    def __radd__(self, other):
        return self + other
