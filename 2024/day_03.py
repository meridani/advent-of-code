import aoc_helper
from rich.progress import track

DAY = 3


def parse_raw(inp: str):
    return inp


def parse_raw2(inp: str):
    return parse_raw(inp)


def part_one(data):
    return


aoc_helper.lazy_test(day=3, year=2024, parse=parse_raw, solution=part_one)


def part_two(data):
    return


if __name__ == "__main__":

    raw = aoc_helper.fetch(DAY, 2024)

    aoc_helper.lazy_test(day=DAY, year=2024, parse=parse_raw, solution=part_one)
    aoc_helper.lazy_test(day=DAY, year=2024, parse=parse_raw2, solution=part_two)

    parsed = parse_raw(raw)

    aoc_helper.lazy_submit(day=DAY, year=2024, solution=part_one, data=parsed)

    parsed = parse_raw2(raw)

    aoc_helper.lazy_submit(day=DAY, year=2024, solution=part_two, data=parsed)
