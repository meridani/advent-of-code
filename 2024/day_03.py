import aoc_helper
from rich.progress import track
import re

DAY = 3


def parse_raw(inp: str):
    pattern = re.compile(r"mul\((\d+),(\d+)\)")
    matches = pattern.findall(inp)
    nums = []
    for match in matches:
        nums.append(tuple(int(x) for x in match))
    return nums


def parse_raw2(inp: str):
    parts = inp.split("do()")
    parts = [part.split("don't()")[0] for part in parts]
    parts = "".join(parts)
    return parse_raw(parts)


def part_one(data):
    sums = 0
    for a, b in data:
        sums += a * b

    print(sums)
    return sums


def part_two(data):
    sums = part_one(data)
    return sums


if __name__ == "__main__":

    raw = aoc_helper.fetch(DAY, 2024)
    parsed = parse_raw(raw)

    aoc_helper.lazy_test(day=DAY, year=2024, parse=parse_raw, solution=part_one)
    aoc_helper.lazy_test(day=DAY, year=2024, parse=parse_raw2, solution=part_two)

    aoc_helper.lazy_submit(day=DAY, year=2024, solution=part_one, data=parsed)

    parsed = parse_raw2(raw)

    aoc_helper.lazy_submit(day=DAY, year=2024, solution=part_two, data=parsed)
