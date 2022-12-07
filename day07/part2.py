from __future__ import annotations

import os
from pathlib import Path

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
MAX_SIZE = 100_000
TOTAL_SPACE = 70_000_000
NEED_UNUSED = 30_000_000


class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    @classmethod
    def from_str(cls, input: str):
        size, name = input.strip().split()
        return cls(name, int(size))

    def __str__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other: File):
        return self.name == other.name


class FSNavigator:
    def __init__(self):
        self.curr_dir: Path | None = None
        self.dirs: dict[str, set[File]] = {}

    def cd(self, path: str) -> Path:
        if self.curr_dir is None:
            self.curr_dir = Path(path)
        else:
            self.curr_dir /= path
        return self.curr_dir.resolve()

    def add_file(self, file: File):
        self.dirs.setdefault(str(self.curr_dir.resolve()), set()).add(file)


def compute(s: str) -> int:
    nav = FSNavigator()
    dirs = set()
    in_ls = False
    for line in s.splitlines():
        if line.startswith("$ cd "):
            dirs.add(str(nav.cd(line[5:])))

        if line.startswith("$"):
            in_ls = False
        elif in_ls and not line.startswith("dir "):
            file = File.from_str(line)
            nav.add_file(file)

        if line == "$ ls":
            in_ls = True

    def size(dir: str):
        dir_size = 0
        for path, files in nav.dirs.items():
            if path.startswith(dir):
                dir_size += sum(file.size for file in files)
        return dir_size

    used_space = size("/")
    min_to_delete = float("inf")
    for dir in dirs:
        dir_size = 0
        for path, files in nav.dirs.items():
            if path.startswith(dir):
                dir_size += sum(file.size for file in files)
        if dir_size >= NEED_UNUSED - (TOTAL_SPACE - used_space):
            min_to_delete = min(dir_size, min_to_delete)

    return min_to_delete


INPUT_S = '''\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
'''
EXPECTED = 24933642


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
