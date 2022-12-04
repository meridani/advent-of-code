from tokenize import Number
from typing import List

import aoc_helper
from aoc_helper import (Grid, PrioQueue, decode_text, extract_ints, frange,
                        irange, iter, list, map, range, tail_call)

raw = aoc_helper.fetch(4, 2022)


def parse_raw() -> List:
    elfs = [[list(map(int, elf.split("-"))) for elf in line.split(",")]for line in raw.splitlines()]

    return elfs

data: List = parse_raw()

def overlap_partial(elf: List) -> Number:
    if elf[0][0] in range(elf[1][0],elf[1][1]):
        return 1
    if elf[0][1] in range(elf[1][0], elf[1][1]):
        return 1
    if overlap(elf):
        return 1
    return 0


def overlap(elf: List) -> Number:
    # elf 0 kissebb
    if elf[0][0] <= elf[1][0] and elf[0][1] >= elf[1][1]:
        return 1
    elif elf[0][0] >= elf[1][0] and elf[0][1] <= elf[1][1]:
        return 1
    return 0


def part_one():
    sums: Number = 0
    for elf in data:
        sums += overlap(elf)
    return sums


def part_two():
    sums: Number = 0
    for elf in data:
        sums += overlap_partial(elf)

    return sums

def test_ex1():
    global raw
    global data
    raw = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
    data = parse_raw()
    assert(part_one()==2)
    assert(part_two()==4)

if __name__ == "__main__":
    aoc_helper.lazy_submit(day=4, year=2022, solution=part_one)
    aoc_helper.lazy_submit(day=4, year=2022, solution=part_two)
