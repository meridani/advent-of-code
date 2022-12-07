from collections import defaultdict
from enum import Enum
from operator import le
from sys import maxsize
from typing import List

import aoc_helper
from aoc_helper import (Grid, PrioQueue, decode_text, extract_ints, frange,
                        irange, iter, list, map, range, tail_call)


class FileType(Enum):
    FILE = 1
    DIRECTORY = 2


class FileNode:
    def __init__(self, name: str, parent = None, type: FileType = FileType.DIRECTORY,  size: int = 0) -> None:
        self.children = defaultdict(FileNode)
        self.parent: FileNode = parent
        self.name: str = name
        self.type: FileType = type
        self.size: int = size

    def addChild(self, node):
        self.children[node.name] = node
        self.size += node.size
        root = self
        while root.parent:
            root.parent.size += node.size
            root = root.parent

    def __iter__(self):
        yield self
        for c in self.children.values():
            yield from c

    def __setitem__(self, name, node):
        self.children[name] = node

    def __getitem__(self, name):
        return self.children[name]

    def __contains__(self, name):
        return name in self.children

    def __hash__(self) -> int:
        return hash(self.name) + hash(self.parent)

    def __str__(self):
        return self.name

    def __repr__(self) -> str:
        return (f"{self.name}, size: {self.size}, type: {self.type}")


def parse_raw(raw):
    lines = raw.splitlines()
    root = FileNode(name="/")
    pwd = root
    for line in lines:
        parts = line.split()

        match parts[0]:
            case "$":
                match parts[1]:
                    case "cd":
                        match parts[2]:
                            case "/": pwd = root
                            case "..": pwd = pwd.parent if pwd.parent else pwd
                            case _: pwd = pwd[parts[2]]

                    case "ls":
                        ...
            case "dir":
                newNode = FileNode(name=parts[1], parent=pwd)
                pwd.addChild(newNode)
            case _:
                newNode = FileNode(name=parts[1], parent=pwd, type=FileType.FILE, size=int(parts[0]))
                pwd.addChild(newNode)
    return root


data: FileNode


def part_one():
    global data
    sum = 0

    for c in data:
        if c.type == FileType.DIRECTORY and c.size <= 100000:
            sum += c.size
    return sum


def part_two():
    global data
    max_size = 70000000
    min_free = 30000000

    to_delete = data
    for c in data:
        if c.type == FileType.DIRECTORY and c.size > data.size + min_free - max_size and to_delete.size > c.size:
            to_delete = c

    return to_delete.size


def test_ex1():
    raw = """$ cd /
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
7214296 k"""
    global data
    data = parse_raw(raw)
    assert data.size == 48381165
    assert (part_one() == 95437)
    assert (part_two() == 24933642)


if __name__ == "__main__":
    # test_ex1()
    raw = aoc_helper.fetch(7, 2022)
    data = parse_raw(raw)
    p1 = part_one()
    p2 = part_two()
    print(p1)
    print(p2)
    try:
        aoc_helper.lazy_submit(day=7, year=2022, solution=part_one)
        aoc_helper.lazy_submit(day=7, year=2022, solution=part_two)
    except:
        print("Can't upload to AoC")
