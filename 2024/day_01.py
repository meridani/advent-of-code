from collections import defaultdict, deque
from typing import TYPE_CHECKING

import aoc_helper

DAY = 1


def parse_raw(raw: str):

    data = []
    left, right = [], []
    for line in raw.splitlines():
        a, b = [int(x) for x in line.split()]
        left.append(a)
        right.append(b)

    left.sort()
    right.sort()
    return zip(left, right)


def parse_raw2(raw: str):
    return parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data):
    sums = 0
    diffs = [abs(x - y) for x, y in data]
    sums = sum(diffs)

    return sums


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data):
    left, right = zip(*data)

    sums = 0
    for x in left:
        count = right.count(x)
        sums += count * x

    return sums


if __name__ == "__main__":

    raw = aoc_helper.fetch(DAY, 2024)
    parsed = parse_raw(raw)

    part1 = part_one(parsed)
    aoc_helper.lazy_test(day=DAY, year=2024, parse=parse_raw, solution=part_one)
    aoc_helper.submit(DAY, 2024, part1)

    parsed = parse_raw2(raw)

    part2 = part_two(parsed)
    aoc_helper.lazy_test(day=DAY, year=2024, parse=parse_raw2, solution=part_two)
    aoc_helper.submit(DAY, 2024, part2)
