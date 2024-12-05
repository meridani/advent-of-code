import aoc_helper
from tqdm import tqdm

DAY = 5


def parse_raw(inp: str):
    rules = []
    orders = []
    for line in inp.splitlines():
        if "|" in line:
            parts = [int(x) for x in line.split("|")]
            rules.append(parts)
        elif "," in line:
            parts = [int(x) for x in line.split(",")]
            orders.append(parts)

    return rules, orders


def parse_raw2(inp: str):
    return parse_raw(inp)


def part_one(data):
    answer = 0
    rules, orders = data

    for order in orders:
        ok = True
        for rule in rules:
            if rule[0] in order and rule[1] in order:
                pos1 = order.index(rule[0])
                pos2 = order.index(rule[1])
                if pos1 > pos2:
                    ok = False
                    break
        if ok:
            middle_index = len(order) // 2
            answer += order[middle_index]

    return answer


def part_two(data):
    answer = 0
    rules, orders = data

    for order in tqdm(orders):
        if not ordered(rules, order):
            reorder(rules, order)
            middle_index = len(order) // 2
            answer += order[middle_index]

    return answer


def reorder(rules, order):
    ok = False
    while not ok:
        for rule in rules:
            if rule[0] in order and rule[1] in order:
                pos1 = order.index(rule[0])
                pos2 = order.index(rule[1])
                if pos1 > pos2:
                    order[pos1], order[pos2] = order[pos2], order[pos1]
        if ordered(rules, order):
            ok = True
    return order


def ordered(rules, order):
    for rule in rules:
        if rule[0] in order and rule[1] in order:
            pos1 = order.index(rule[0])
            pos2 = order.index(rule[1])
            if pos1 > pos2:
                return False
    return True


if __name__ == "__main__":

    raw = aoc_helper.fetch(DAY, 2024)
    parsed = parse_raw(raw)

    part1 = part_one(parsed)
    aoc_helper.lazy_test(day=DAY, year=2024, parse=parse_raw, solution=part_one)
    aoc_helper.submit(day=DAY, year=2024, part=1, answer=part1)

    parsed = parse_raw2(raw)

    part2 = part_two(parsed)
    aoc_helper.lazy_test(day=DAY, year=2024, parse=parse_raw2, solution=part_two)
    aoc_helper.submit(day=DAY, year=2024, part=2, answer=part2)
