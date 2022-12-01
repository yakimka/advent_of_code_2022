from __future__ import annotations

from typing import Generator


def parse_numbers_split_new_line(s: str) -> Generator[int | None, None, None]:
    for line in s.splitlines():
        try:
            yield int(line)
        except ValueError:
            yield None
