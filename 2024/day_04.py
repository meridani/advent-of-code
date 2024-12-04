import aoc_helper
from rich.progress import track
import numpy as np

DAY = 4


def parse_raw(inp: str):
    table = np.array([list(i) for i in inp.splitlines()])
    return table


def parse_raw2(inp: str):

    return parse_raw(inp)


def part_one(data):
    sums = 0
    h, w = len(data), len(data[0])
    for row in range(h):
        sums += "".join(data[row]).count("XMAS")
        sums += "".join(data[row]).count("SAMX")
        sums += "".join(data[:, row]).count("XMAS")
        sums += "".join(data[:, row]).count("SAMX")

    for col in range(-w - h + 1, w + h):
        sums += "".join(data.diagonal(col)).count("XMAS")
        sums += "".join(data.diagonal(col)).count("SAMX")
        sums += "".join(np.fliplr(data).diagonal(col)).count("XMAS")
        sums += "".join(np.fliplr(data).diagonal(col)).count("SAMX")

    print(sums)
    return sums


def part_two(data):
    sums = 0
    h, w = len(data), len(data[0])

    for row in range(1, h - 1):
        for col in range(1, w - 1):
            if data[row][col] == "A":
                if (
                    data[row - 1][col - 1] == "M"
                    and data[row + 1][col + 1] == "S"
                    and data[row - 1][col + 1] == "M"
                    and data[row + 1][col - 1] == "S"
                ):
                    sums += 1
                elif (
                    data[row - 1][col - 1] == "S"
                    and data[row + 1][col + 1] == "M"
                    and data[row - 1][col + 1] == "M"
                    and data[row + 1][col - 1] == "S"
                ):
                    sums += 1
                elif (
                    data[row - 1][col - 1] == "M"
                    and data[row + 1][col + 1] == "S"
                    and data[row - 1][col + 1] == "S"
                    and data[row + 1][col - 1] == "M"
                ):
                    sums += 1
                elif (
                    data[row - 1][col - 1] == "S"
                    and data[row + 1][col + 1] == "M"
                    and data[row - 1][col + 1] == "S"
                    and data[row + 1][col - 1] == "M"
                ):
                    sums += 1

    print(sums)
    return sums


if __name__ == "__main__":

    raw = aoc_helper.fetch(DAY, 2024)
    parsed = parse_raw(raw)

    aoc_helper.lazy_test(day=DAY, year=2024, parse=parse_raw, solution=part_one)
    aoc_helper.lazy_test(day=DAY, year=2024, parse=parse_raw2, solution=part_two)

    aoc_helper.lazy_submit(day=DAY, year=2024, solution=part_one, data=parsed)

    parsed = parse_raw2(raw)

    aoc_helper.lazy_submit(day=DAY, year=2024, solution=part_two, data=parsed)