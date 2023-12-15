import functools
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

raw = aoc_helper.fetch(15, 2023)


def parse_raw(raw: str):
    return raw


data = parse_raw(raw)


def holiday_hash(label: str) -> int:
    return functools.reduce(lambda x, y: (x + y) * 17 % 256, map(ord, label), 0)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    return sum((holiday_hash(label) for label in data.split(",")))


aoc_helper.lazy_test(day=15, year=2023, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    boxes: defaultdict(int, dict(int, str)) = defaultdict(dict)

    for step in data.split(","):
        if "=" in step:
            label, power = step.split("=")
            boxes[holiday_hash(label)][label] = int(power)
        else:
            label = step.strip("-")
            boxes[holiday_hash(label)].pop(label, None)

    return sum(
        sum((box + 1) * pos * focal for pos, focal in enumerate(lenses.values(), 1))
        for box, lenses in boxes.items()
    )


print(part_one())
print(part_two())

aoc_helper.lazy_test(day=15, year=2023, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=15, year=2023, solution=part_one, data=data)
aoc_helper.lazy_submit(day=15, year=2023, solution=part_two, data=data)
