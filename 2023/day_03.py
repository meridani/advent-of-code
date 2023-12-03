from collections import defaultdict, deque
from math import prod
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

raw = aoc_helper.fetch(3, 2023)


def classifier(char: str, /) -> int:
    return char


def parse_raw(raw: str):
    grid = Grid("").from_string(raw, classifier)
    return grid


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    nr_list = []
    for y, row in enumerate(data):
        for x, char in enumerate(row):
            if char not in "0123456789.":
                n = data.neighbours(y, x)
                for loc, _ in n:
                    y_ = loc[0]
                    x_ = loc[1]
                    if data[y_][x_] in "0123456789":
                        while x_ != 0:
                            if data[y_][x_ - 1] in "0123456789":
                                x_ -= 1
                            else:
                                break

                        nr_list.append((x_, y_))
    nr_list = list(set(nr_list))
    sums = 0
    for x, y in nr_list:
        num = ""
        while data[y][x] in "0123456789":
            num += data[y][x]
            x += 1
            if x >= len(data[y]):
                break
        sums += int(num)
    return sums


aoc_helper.lazy_test(day=3, year=2023, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    sums = 0
    for y, row in enumerate(data):
        for x, char in enumerate(row):
            if char == "*":
                nr_list = []
                n = data.neighbours(y, x)
                for loc, _ in n:
                    y_ = loc[0]
                    x_ = loc[1]
                    if data[y_][x_] in "0123456789":
                        while x_ != 0:
                            if data[y_][x_ - 1] in "0123456789":
                                x_ -= 1
                            else:
                                break

                        nr_list.append((x_, y_))
                nr_list = list(set(nr_list))
                if len(nr_list) == 2:
                    nums = []
                    for x_, y_ in nr_list:
                        num = ""
                        while data[y_][x_] in "0123456789":
                            num += data[y_][x_]
                            x_ += 1
                            if x_ >= len(data[y_]):
                                nums.append(int(num))
                                break
                        nums.append(int(num))
                    sums += prod(nums)
    return sums


aoc_helper.lazy_test(day=3, year=2023, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=3, year=2023, solution=part_one, data=data)
aoc_helper.lazy_submit(day=3, year=2023, solution=part_two, data=data)
