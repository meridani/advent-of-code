import copy
import re
from typing import List

import aoc_helper
from aoc_helper import (Grid, PrioQueue, decode_text, extract_ints, frange,
                        irange, iter, list, map, range, tail_call)

raw = aoc_helper.fetch(5, 2022)

crates = [[], [], [], [], [], [], [], [], []]
crates2: List
moves = []

def parse_raw():
    for line in raw.splitlines():
        if line.startswith("move"):
            moves.append(list(map(int, (re.findall(r'\d+', line)))))
        else:
            c = line[1::4]
            [crates[id].append(item) if item.isalpha() else ... for id, item in enumerate(c)]
    
    for c in crates:
        c.reverse()
    
    global crates2
    crates2 = copy.deepcopy(crates)
    return


def move(l: List, m: List, capacity=1) -> List:
    (num, src, dest) = m[0], m[1]-1, m[2]-1

    h = l[src][-num:]
    del l[src][-num:]
    if capacity == 1:
        h.reverse()
    l[dest].extend(h)
    return l

def part_one():
    global crates
    for m in moves:
        crates = move(crates, m)

    return ''.join([c.pop() for c in crates if c])


def part_two():
    global crates2
    for m in moves:
        crates2 = move(crates2, m, 10)

    return ''.join([c.pop() for c in crates2 if c])


def test_ex1():
    global data
    global raw
    raw = """            [L] [M]         [M]    
        [D] [R] [Z]         [C] [L]
        [C] [S] [T] [G]     [V] [M]
[R]     [L] [Q] [B] [B]     [D] [F]
[H] [B] [G] [D] [Q] [Z]     [T] [J]
[M] [J] [H] [M] [P] [S] [V] [L] [N]
[P] [C] [N] [T] [S] [F] [R] [G] [Q]
[Z] [P] [S] [F] [F] [T] [N] [P] [W]
 1   2   3   4   5   6   7   8   9 

move 6 from 3 to 9"""
    data = parse_raw()
    assert (part_two() == "RBSLMGVMD")


if __name__ == "__main__":
    parse_raw()
    aoc_helper.lazy_submit(day=5, year=2022, solution=part_one)
    aoc_helper.lazy_submit(day=5, year=2022, solution=part_two)
