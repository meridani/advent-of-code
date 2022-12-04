import aoc_helper
from aoc_helper import (Grid, PrioQueue, decode_text, extract_ints, frange,
                        irange, iter, list, map, range, tail_call)

raw: str = aoc_helper.fetch(1, 2022)


def parse_raw():
    return raw.splitlines()


data = parse_raw()

elves = []

def part_one():
    biggest = 0
    tempsum = 0
    for item in data:
        if item != "":
            tempsum = tempsum + int(item)
        else:
            if tempsum > biggest:
                biggest = tempsum
            elves.append(tempsum)
            tempsum = 0
    return max(elves)


def part_two():
    elves.sort()
    return sum(elves[-3:])


if __name__ == "__main__":
    aoc_helper.lazy_submit(day=1, year=2022, solution=part_one)
    aoc_helper.lazy_submit(day=1, year=2022, solution=part_two)
