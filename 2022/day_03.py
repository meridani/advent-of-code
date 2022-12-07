from tokenize import Number
from typing import List

import aoc_helper

raw = aoc_helper.fetch(3, 2022)


def parse_raw(raw) -> List:
    # pass
    return raw.splitlines()
    # return [line.split(" ") for line in raw.splitlines()]


data: List


def part_one() -> Number:
    sums: Number = 0

    for line in data:
        line_len: int = int(len(line)/2)  # noqa: F821
        part1 = {*line[:line_len]}
        part2 = {*line[line_len:]}
        part1.intersection_update(part2)
        for item in part1:
            priority = ord(item)-ord('A') + 27 if item.isupper() else ord(item)-ord('a') + 1
            sums += priority

    return sums


def part_two() -> Number:
    sums: Number = 0

    group_pos: Number = 0
    groups = [{}, {}, {}]

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
    global data
    raw = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
    data = parse_raw(raw)
    assert (part_one() == 157)
    assert (part_two() == 70)


if __name__ == "__main__":
    data = parse_raw(raw)
    aoc_helper.lazy_submit(day=3, year=2022, solution=part_one)
    aoc_helper.lazy_submit(day=3, year=2022, solution=part_two)
