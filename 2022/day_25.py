from typing import List

import aoc_helper
from aoc_helper import (Grid, PrioQueue, decode_text, extract_ints, frange,
                        irange, iter, list, map, range, tail_call)

raw = aoc_helper.fetch(25, 2022)


def parse_raw() -> List:
    pass
    # return [line.split(" ") for line in raw.splitlines()]

data: List = parse_raw()

def part_one():
    pass

def part_two():
    pass

def test_ex1():
    global raw
    global data
    raw=""""""
    data = parse_raw()
    assert(part_one()==1)
    assert(part_two()==1)


if __name__ == "__main__":
    aoc_helper.lazy_submit(day=25, year=2022, solution=part_one)
    aoc_helper.lazy_submit(day=25, year=2022, solution=part_two)
