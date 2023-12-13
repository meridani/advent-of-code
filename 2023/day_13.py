from collections import defaultdict, deque
from typing import TYPE_CHECKING
import numpy
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

raw = aoc_helper.fetch(13, 2023)


def parse_raw(raw: str):
    notes = raw.split("\n\n")
    return notes


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    
    sums = 0

    for grid in data:
        g = numpy.array([[x == "#" for x in l] for l in grid.split()])
        for i in range(1, len(g)):
            j = min(i, len(g) - i)
            # print()
            # print(a[:i])
            # print(a[:i][::-1])
            # print(a[:i][::-1][:n])
            # print(a[i:][:n])
            normal = g[i:]
            rev = g[:i][::-1]
            if numpy.sum(rev[:j] ^ normal[:j]) == 0:
                sums += i*100
        g = g.T
        for i in range(1, len(g)):
            j = min(i, len(g) - i)
            normal = g[i:]
            rev = g[:i][::-1]
            if numpy.sum(rev[:j] ^ normal[:j]) == 0:
                sums += i
    return sums
print(part_one())
aoc_helper.lazy_test(day=13, year=2023, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    
    sums = 0

    for grid in data:
        g = numpy.array([[x == "#" for x in l] for l in grid.split()])
        for i in range(1, len(g)):
            j = min(i, len(g) - i)
            normal = g[i:]
            rev = g[:i][::-1]
            if numpy.sum(rev[:j] ^ normal[:j]) == 1:
                sums += i*100
        g = g.T
        for i in range(1, len(g)):
            j = min(i, len(g) - i)
            normal = g[i:]
            rev = g[:i][::-1]
            if numpy.sum(rev[:j] ^ normal[:j]) == 1:
                sums += i
    return sums
print(part_two())

aoc_helper.lazy_test(day=13, year=2023, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=13, year=2023, solution=part_one, data=data)
aoc_helper.lazy_submit(day=13, year=2023, solution=part_two, data=data)
