from collections import defaultdict, deque
from typing import TYPE_CHECKING

import aoc_helper
from aoc_helper import (
    Grid,
    PrioQueue,
    SparseGrid,
    decode_text,
    extract_ints,
    extract_iranges,
    extract_ranges,
    extract_uints,
    frange,
    irange,
    iter,
    list,
    map,
    range,
    search,
    tail_call,
)

raw = aoc_helper.fetch(1, 2024)


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


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    sums = 0
    diffs = [abs(x - y) for x, y in data]
    sums = sum(diffs)
    print(sums)

    return sums


aoc_helper.lazy_test(day=1, year=2024, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    left, right = zip(*data)

    sums = 0
    for x in left:
        count = right.count(x)
        sums += count * x

    print(sums)
    return sums


aoc_helper.lazy_test(day=1, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=1, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=1, year=2024, solution=part_two, data=data)
