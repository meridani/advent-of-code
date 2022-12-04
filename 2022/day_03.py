from tokenize import Number, group
from typing import List

import aoc_helper
from aoc_helper import (Grid, PrioQueue, decode_text, extract_ints, frange,
                        irange, iter, list, map, range, tail_call)

raw = aoc_helper.fetch(3, 2022)


def parse_raw() -> List:
    # pass
    return raw.splitlines()
    # return [line.split(" ") for line in raw.splitlines()]

data: List = parse_raw()

def part_one() -> Number:
    sums: Number = 0

    for line in data:
        l = int(len(line)/2)
        part1 = {*line[:l]}
        part2 = {*line[l:]}
        part1.intersection_update(part2)
        for item in part1:
            priority = ord(item)-ord('A') + 27 if item.isupper() else ord(item)-ord('a') + 1
            sums += priority


    return sums

def part_two() -> Number:
    sums: Number = 0

    group_pos:Number = 0
    groups = [{},{},{}]

    for line in data:
        groups[group_pos] = {*line}
        group_pos += 1
        if group_pos == 3:
            group_pos = 0
            groups[0].intersection_update(groups[1])
            groups[0].intersection_update(groups[2])
            badge = groups[0].pop()
            priority = ord(badge)-ord('A') + 27 if badge.isupper() else ord(badge)-ord('a') + 1
            sums += priority

    return sums

def test_ex1():
    global raw
    global data
    raw="""vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
    data = parse_raw()
    assert(part_one()==157)
    assert(part_two()==70)


if __name__ == "__main__":
    aoc_helper.lazy_submit(day=3, year=2022, solution=part_one)
    aoc_helper.lazy_submit(day=3, year=2022, solution=part_two)
