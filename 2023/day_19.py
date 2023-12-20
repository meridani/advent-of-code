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

raw = aoc_helper.fetch(19, 2023)


def parse_raw(raw: str):
    w, parts = raw.split("\n\n")
    workflows = {}
    for workflow in w.splitlines():
        name, rules = workflow.strip("}").split("{")
        rules = rules.split(",")
        comps = []
        for rule in rules:
            category = rule[0:1]
            op = rule[1:2]
            t = rule[2:].split(":")
            if len(t) > 1:
                value, target = t
            else:
                target = rule
            comp = (category, op, int(value), target)
            comps.append(comp)
        workflows[name] = comps

    parts = [
        {p.split("=")[0]: int(p.split("=")[1]) for p in part.strip("{}").split(",")}
        for part in parts.splitlines()
    ]

    return workflows, parts


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    workflows, parts = data

    sums = 0

    for part in parts:
        curr_work = workflows["in"]

        run = True
        while run:
            for category, op, val, target in curr_work:
                if category == "A":
                    sums += sum(part.values())
                    run = False
                    break
                if category == "R":
                    run = False
                    break

                match op:
                    case "<":
                        if part[category] < val:
                            if target == "R":
                                run = False
                                break
                            elif target == "A":
                                sums += sum(part.values())
                                run = False
                                break
                            else:
                                curr_work = workflows[target]
                            break
                        else:
                            continue
                    case ">":
                        if part[category] > val:
                            if target == "R":
                                run = False
                                break
                            elif target == "A":
                                sums += sum(part.values())
                                run = False
                                break
                            else:
                                curr_work = workflows[target]
                            break
                        else:
                            continue

            else:
                curr_work = workflows[target]
    return sums


print(part_one())
# aoc_helper.lazy_test(day=19, year=2023, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    workflows, _ = data
    values = set()
    curr_work = workflows["in"]
    run = True
    while run:
        for category, op, val, target in curr_work:
            if category == "A":
                run = False
                break
            if category == "R":
                run = False
                break

            match op:
                case "<":
                    ...
                case ">":
                    ...

        else:
            curr_work = workflows[target]


print(part_two())

# aoc_helper.lazy_test(day=19, year=2023, parse=parse_raw, solution=part_two)

# aoc_helper.lazy_submit(day=19, year=2023, solution=part_one, data=data)
# aoc_helper.lazy_submit(day=19, year=2023, solution=part_two, data=data)
