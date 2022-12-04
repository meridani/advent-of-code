from typing import List

import aoc_helper
from aoc_helper import (Grid, PrioQueue, decode_text, extract_ints, frange,
                        irange, iter, list, map, range, tail_call)

raw = aoc_helper.fetch(2, 2022)


def parse_raw() -> List:
    return [line.split(" ") for line in raw.splitlines()]

data: List = parse_raw()

def part_one():
    score = 0
    for line in data:
        opponent = ord(line[0]) - ord('A')
        you = ord(line[1]) - ord('X')
        s = (you - opponent) % 3
        score += you + 1
        score += 3 + s * 3 if s < 2 else 0

    return score


def part_two():
    score = 0
    for line in data:
        opponent = ord(line[0]) - ord('A')
        outcome = ord(line[1]) - ord('Y')
        draw = (opponent + outcome) % 3
        score += (outcome + 1) * 3
        score += draw + 1

    return score

def test_ex1():
    global raw
    global data
    raw="""A Y
B X
C Z"""
    data = parse_raw()
    assert(part_one()==15)
    assert(part_two()==12)


if __name__ == "__main__":
    aoc_helper.lazy_submit(day=2, year=2022, solution=part_one)
    aoc_helper.lazy_submit(day=2, year=2022, solution=part_two)
