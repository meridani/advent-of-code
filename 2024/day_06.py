import aoc_helper
from rich import pretty, print
from rich.traceback import install

install(show_locals=False)

DAY = 6


def parse_raw(inp: str): ...


def parse_raw2(inp: str):
    return parse_raw(inp)


def part_one(data):
    answer = 0
    return answer


def part_two(data):
    answer = 0
    return answer


if __name__ == "__main__":

    raw = aoc_helper.fetch(DAY, 2024)
    parsed = parse_raw(raw)

    part1 = part_one(parsed)
    try:
        aoc_helper.lazy_test(day=DAY, year=2024, parse=parse_raw, solution=part_one)
        aoc_helper.submit(day=DAY, year=2024, part=1, answer=part1)
    except:
        print(part1)

    parsed = parse_raw2(raw)

    part2 = part_two(parsed)

    try:
        aoc_helper.lazy_test(day=DAY, year=2024, parse=parse_raw2, solution=part_two)
        aoc_helper.submit(day=DAY, year=2024, part=2, answer=part2)
    except:
        print(part2)
