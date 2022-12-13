import aoc_helper
from aoc_helper import (Grid, PrioQueue, decode_text, extract_ints, frange,
                        irange, iter, list, map, range, tail_call)


def parse_raw(raw):
    return raw

def part_one():
    ...


def part_two():
    ...

def test_ex1():
    raw=""""""
    global data
    data = parse_raw(raw)
    assert(part_one()==0)
    assert(part_two()==0)

if __name__ == "__main__":
    raw = aoc_helper.fetch(14, 2022)
    data = parse_raw(raw)
    try:
        aoc_helper.lazy_submit(day=14, year=2022, solution=part_one)
        aoc_helper.lazy_submit(day=14, year=2022, solution=part_two)
    except Exception as err:
        print("Can't upload to AoC", err)