import aoc_helper
from rich.progress import track

DAY = 2


def is_valid(report):
    increasing = all(
        report[i] < report[i + 1] and 1 <= report[i + 1] - report[i] <= 3
        for i in range(len(report) - 1)
    )
    decreasing = all(
        report[i] > report[i + 1] and 1 <= report[i] - report[i + 1] <= 3
        for i in range(len(report) - 1)
    )
    return increasing or decreasing


def parse_raw(inp: str):
    reports = []
    for line in inp.splitlines():
        reports.append([int(x) for x in line.split()])

    return reports


def parse_raw2(inp: str):
    return parse_raw(inp)


def part_one(data):
    sums = 0
    for report in track(data):
        if is_valid(report):
            sums += 1

    return sums


def part_two(data):

    sums = 0
    for report in track(data):

        if is_valid(report):
            sums += 1
        else:
            for i in range(len(report)):
                modified_report = report[:i] + report[i + 1 :]
                if is_valid(modified_report):
                    sums += 1
                    break

    return sums


if __name__ == "__main__":

    raw = aoc_helper.fetch(DAY, 2024)

    aoc_helper.lazy_test(day=DAY, year=2024, parse=parse_raw, solution=part_one)
    aoc_helper.lazy_test(day=DAY, year=2024, parse=parse_raw2, solution=part_two)

    parsed = parse_raw(raw)

    aoc_helper.lazy_submit(day=DAY, year=2024, solution=part_one, data=parsed)

    parsed = parse_raw2(raw)

    aoc_helper.lazy_submit(day=DAY, year=2024, solution=part_two, data=parsed)
