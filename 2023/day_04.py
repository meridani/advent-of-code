from collections import defaultdict, deque
from time import perf_counter
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

raw = aoc_helper.fetch(4, 2023)


def profiler(method):
    def wrapper_method(*arg, **kw):
        t = perf_counter()
        ret = method(*arg, **kw)
        print(
            "Method "
            + method.__name__
            + " took : "
            + "{:2.5f}".format(perf_counter() - t)
            + " sec"
        )
        return ret

    return wrapper_method


@profiler
def parse_raw(raw: str):
    nr_list = []
    for line in raw.splitlines():
        nr_list.append(extract_uints(line))
    return nr_list


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    sums = 0
    for line in data:
        winning = set(line[1:11])
        numbers = set(line[11:])
        before = len(numbers)
        numbers.update(winning)
        after = len(numbers)
        winning = 10 - (after - before)
        points = 0
        if winning > 0:
            points = pow(2, winning - 1)
        sums += points
    return sums


# aoc_helper.lazy_test(day=4, year=2023, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
@profiler
def part_two(data=data):
    sums = 0
    wins = []
    for i, line in enumerate(data):
        # winning = set(line[1:6])
        # numbers = set(line[6:])
        winning = set(line[1:11])
        numbers = set(line[11:])
        before = len(numbers)
        numbers.update(winning)
        after = len(numbers)
        winning = 10 - (after - before)
        wins.append((winning, 1))

    for i, win in enumerate(wins):
        if win[0] > 0:
            for j in range(win[0]):
                if i + j + 1 < len(wins):
                    new_win = (wins[i + j + 1][0], wins[i + j + 1][1] + win[1])
                    wins[i + j + 1] = new_win
    for win in wins:
        sums += win[1]
    return sums


# aoc_helper.lazy_test(day=4, year=2023, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=4, year=2023, solution=part_one, data=data)
aoc_helper.lazy_submit(day=4, year=2023, solution=part_two, data=data)
