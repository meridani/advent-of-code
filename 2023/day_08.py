from collections import defaultdict, deque, namedtuple
from math import lcm
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

raw = aoc_helper.fetch(8, 2023)

NODE = namedtuple("Node", "L R")

def parse_raw(raw: str):

    nodes = {}

    instruction, rows = raw.split("\n\n")
    for row in rows.splitlines():
        node, dest = row.split(" = ")
        left, right = dest.strip()[1:-1].split(", ")
        nodes[node]=NODE(left,right)

    return instruction, nodes


data = parse_raw(raw)

def run(instruction, nodes, node, end):
    sums = 0
    
    # Nice
    while True:
        for i in instruction:
            sums += 1
            if i == "L":
                next_node = nodes[node].L
            else:
                next_node = nodes[node].R
            node = next_node
            if node.endswith(end):
                return sums


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    instruction, nodes = data
    if len(nodes)==8:
        start = '11A'
        end = '11Z'
    else:
        start = 'AAA'
        end = 'ZZZ'
    return run(instruction, nodes, start, end)
    


aoc_helper.lazy_test(day=8, year=2023, parse=parse_raw, solution=part_one)

# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):

    instruction, nodes = data
    node = [node for node in nodes if node.endswith("A")]
    sums = [run(instruction, nodes, n, 'Z') for n in node]
    return lcm(*sums)

print(part_one())
print(part_two())

aoc_helper.lazy_test(day=8, year=2023, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=8, year=2023, solution=part_one, data=data)
aoc_helper.lazy_submit(day=8, year=2023, solution=part_two, data=data)
