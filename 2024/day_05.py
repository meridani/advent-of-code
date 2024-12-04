import aoc_helper
from rich.progress import track
import numpy as np

DAY = 5


def parse_raw(inp: str):
    ret = 0
    return ret


def parse_raw2(inp: str):
    return parse_raw(inp)


def part_one(data):
    answer = 0

    print(answer)
    return answer


def part_two(data):
    answer = 0

    print(answer)
    return answer


if __name__ == "__main__":

    raw = aoc_helper.fetch(DAY, 2024)
    parsed = parse_raw(raw)

    part1 = part_one(parsed)
    aoc_helper.lazy_test(day=DAY, year=2024, parse=parse_raw, solution=part_one)
    aoc_helper.submit(DAY, 2024, part1)

    parsed = parse_raw2(raw)

    part2 = part_two(parsed)
    aoc_helper.lazy_test(day=DAY, year=2024, parse=parse_raw2, solution=part_two)
    aoc_helper.submit(DAY, 2024, part2)
