from collections import defaultdict, deque, Counter
from itertools import combinations
from math import inf
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
    multirange,
    search,
    tail_call,
)

raw = aoc_helper.fetch(11, 2023)


def parse_raw(raw: str):
    # empty_rows = []
    # empty_columns = []

    galaxies = [
        (r, c)
        for r, line in enumerate(raw.splitlines())
        for c, i in enumerate(line)
        if i == "#"
    ]
    empty_rows = {*range(len(raw.splitlines()))} - {r for r, _ in galaxies}
    empty_columns = {*range(len(raw.splitlines()[0]))} - {c for _, c in galaxies}

    return empty_rows, empty_columns, galaxies


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    empty_rows, empty_columns, galaxies = data

    galaxy_pairs = combinations(galaxies, 2)

    sums = 0
    for start, end in galaxy_pairs:
        ar, ac = start
        br, bc = end

        ar, br = min(ar, br), max(ar, br)
        ac, bc = min(ac, bc), max(ac, bc)
        distance = abs(br - ar) + len(empty_rows & set(range(ar, br + 1)))
        distance += abs(bc - ac) + len(empty_columns & set(range(ac, bc + 1)))

        # print(start, end, distance)
        sums += distance
    return sums


aoc_helper.lazy_test(day=11, year=2023, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    empty_rows, empty_columns, galaxies = data

    galaxy_pairs = combinations(galaxies, 2)

    sums = 0
    for start, end in galaxy_pairs:
        ar, ac = start
        br, bc = end

        ar, br = min(ar, br), max(ar, br)
        ac, bc = min(ac, bc), max(ac, bc)

        distance = abs(br - ar) + len(empty_rows & set(range(ar, br + 1))) * (
            1_000_000 - 1
        )
        distance += abs(bc - ac) + len(empty_columns & set(range(ac, bc + 1))) * (
            1_000_000 - 1
        )

        # print(start, end, distance)
        sums += distance
    return sums


print(part_two())
# aoc_helper.lazy_test(day=11, year=2023, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=11, year=2023, solution=part_one, data=data)
aoc_helper.lazy_submit(day=11, year=2023, solution=part_two, data=data)
