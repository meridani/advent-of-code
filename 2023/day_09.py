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

raw = aoc_helper.fetch(9, 2023)


def parse_raw(raw: str):
    readings = []
    for line in raw.splitlines():
        readings.append(extract_ints(line))

    return readings


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    sums = 0
    for reading in data:
        diffs = []
        current = []
        current = numpy.diff(reading)
        diffs.append(current)
        while any(current):
            current = numpy.diff(current)
            diffs.append(current)

        last = 0
        for diff in reversed(diffs):
            last = diff[-1] + last

        sums += reading[-1] + last

    return sums


aoc_helper.lazy_test(day=9, year=2023, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    sums = 0
    for reading in data:
        diffs = []
        current = []
        current = numpy.diff(reading)
        diffs.append(current)
        while any(current):
            current = numpy.diff(current)
            diffs.append(current)

        last = 0
        for diff in reversed(diffs):
            last = diff[0] - last

        sums += reading[0] - last

    return sums


aoc_helper.lazy_test(day=9, year=2023, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=9, year=2023, solution=part_one, data=data)
aoc_helper.lazy_submit(day=9, year=2023, solution=part_two, data=data)
