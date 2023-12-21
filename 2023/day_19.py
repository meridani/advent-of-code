from collections import defaultdict, deque
from copy import deepcopy
from math import prod
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

example = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""


def parse_raw(raw: str):
    w, parts = raw.split("\n\n")
    workflows = {}
    for workflow in w.splitlines():
        name, rules = workflow.strip("}").split("{")
        rules = rules.split(",")
        comps = []
        for rule in rules:
            if ":" in rule:
                category = rule[0:1]
                op = rule[1:2]
                t = rule[2:].split(":")
                if len(t) > 1:
                    value, target = t
                else:
                    target = rule
                comp = (category, op, int(value), target)
                comps.append(comp)
            else:
                comp = (None, None, None, rule)
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


# print(part_one())
# aoc_helper.lazy_test(day=19, year=2023, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    workflows, _ = data
    sums = 0
    q = deque([("in", {category: set(range(1, 4001)) for category in "xmas"})])
    while q:
        curr_work, valid = q.popleft()
        print(f"Doing {curr_work}")
        if curr_work == "R":
            continue
        if curr_work == "A":
            sums += prod(len(valid[category]) for category in valid)
            continue
        for category, op, val, target in workflows[curr_work]:
            print(category, op, val)
            new = deepcopy(valid)
            match op:
                case "<":
                    if target == "R":
                        continue
                    new[category] = new[category] - set(range(val, 4001))
                    if target == "A":
                        sums += prod(len(new[category]) for category in new)
                        break

                case ">":
                    if target == "R":
                        continue
                    new[category] = new[category] - set(range(1, val + 1))
                    if target == "A":
                        print(*(len(new[category]) for category in new))
                        sums += prod(len(new[category]) for category in new)
                        break

            print(
                f"x:{min(new['x']), max(new['x'])}\nm:{min(new['m']), max(new['m'])}\na:{min(new['a']), max(new['a'])}\ns:{min(new['s']), max(new['s'])}"
            )
            print(f"Target: {target}")
            q.append((target, new))
        else:
            ...

    return sums


print(part_two(parse_raw(example)))

# aoc_helper.lazy_test(day=19, year=2023, parse=parse_raw, solution=part_two)

# aoc_helper.lazy_submit(day=19, year=2023, solution=part_one, data=data)
# aoc_helper.lazy_submit(day=19, year=2023, solution=part_two, data=data)
