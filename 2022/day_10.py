from typing import List

import aoc_helper
from aoc_helper import (Grid, PrioQueue, decode_text, extract_ints, frange,
                        irange, iter, list, map, range, tail_call)

raw = aoc_helper.fetch(10, 2022)


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
    # test_ex1()
    p1 = part_one()
    p2 = part_two()
    print(p1)
    print(p2)
    try:
        aoc_helper.lazy_submit(day=10, year=2022, solution=p1)
        aoc_helper.lazy_submit(day=10, year=2022, solution=p2)
    except:
        print("Can't upload to AoC")