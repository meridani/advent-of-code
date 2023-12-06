from collections import defaultdict, deque
from typing import TYPE_CHECKING

from numpy import product
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

raw = aoc_helper.fetch(6, 2023)


def parse_raw(raw: str):
    lines = raw.splitlines()
    times = extract_uints(lines[0])
    distances = extract_uints(lines[1])
    races = zip(times, distances)
    return races


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):

    prod = []
    for t, d in data:
        wins = 0
        for th in range(t):
            distance = th*(t-th)
            if distance > d:
                wins += 1
        prod.append(wins)
    

    return product(prod)

aoc_helper.lazy_test(day=6, year=2023, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    total_t, total_d = "",""
    for t,d in data:
        total_t+=str(t)
        total_d +=str(d)
    t = int(total_t)
    d = int(total_d)

    prod = []
    wins=0
    for th in range(t):
        distance = th*(t-th)
        if distance > d:
            wins += 1
    prod.append(wins)
    

    return product(prod)


aoc_helper.lazy_test(day=6, year=2023, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=6, year=2023, solution=part_one, data=data)
aoc_helper.lazy_submit(day=6, year=2023, solution=part_two, data=data)
