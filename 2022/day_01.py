import aoc_helper
from aoc_helper import (Grid, PrioQueue, decode_text, extract_ints, frange,
                        irange, iter, list, map, range, tail_call)

raw: str = aoc_helper.fetch(1, 2022)


def parse_raw():
    return raw.split("\n\n")


data = parse_raw()

elves = []

def part_one():
    for elf in data:
        items = list(map(int,elf.split()))
        elves.append(sum(items))
    return max(elves)


def part_two():
    elves.sort()
    return sum(elves[-3:])


def test_ex1():
    global raw
    raw="""1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""
    global data
    data = parse_raw()
    assert(part_one()==24000)
    assert(part_two()==45000)

if __name__ == "__main__":
    aoc_helper.lazy_submit(day=1, year=2022, solution=part_one)
    aoc_helper.lazy_submit(day=1, year=2022, solution=part_two)
