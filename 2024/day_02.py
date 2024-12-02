import aoc_helper

raw = aoc_helper.fetch(2, 2024)


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


def parse_raw(raw: str):
    reports = []
    for line in raw.splitlines():
        reports.append([int(x) for x in line.split()])

    return reports


def parse_raw2(raw: str):
    return parse_raw(raw)


data = parse_raw(raw)


def part_one(data=data):
    sums = 0
    for report in data:
        if is_valid(report):
            sums += 1

    return sums


aoc_helper.lazy_test(day=2, year=2024, parse=parse_raw, solution=part_one)
data = parse_raw2(raw)


def part_two(data=data):

    sums = 0
    for report in data:

        if is_valid(report):
            sums += 1
        else:
            for i in range(len(report)):
                modified_report = report[:i] + report[i + 1 :]
                if is_valid(modified_report):
                    sums += 1
                    break

    return sums


aoc_helper.lazy_test(day=2, year=2024, parse=parse_raw2, solution=part_two)

aoc_helper.lazy_submit(day=2, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=2, year=2024, solution=part_two, data=data)
