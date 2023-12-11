from collections import defaultdict, deque, Counter
from math import inf
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
    multirange,
    search,
    tail_call,
)

raw = aoc_helper.fetch(10, 2023)


def parse_raw(raw: str):
    data = []
    start = (0, 0)
    for y, line in enumerate(raw.splitlines()):
        if "S" in line:
            start = (line.index("S"), y)
        data.append(list(line))

    return data, start


data = parse_raw(raw)

NORTH = (0, -1)
EAST = (1, 0)
SOUTH = (0, 1)
WEST = (-1, 0)
valid_moves = {
    "X": [EAST, WEST],  # Manually looked at the input file...
    "|": [NORTH, SOUTH],
    "-": [EAST, WEST],
    "L": [NORTH, EAST],
    "J": [NORTH, WEST],
    "7": [SOUTH, WEST],
    "F": [SOUTH, EAST],
}
NEIGHBOURGHS = [NORTH, EAST, SOUTH, WEST]

FILLED = "█"


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    visited = {}
    start = data[1]
    grid = data[0]
    q = deque()
    max_dist = -inf
    q.append((start, "X", 0))
    visited[start] = 0
    while q:
        node, typ, dist = q.popleft()
        max_dist = max(dist, max_dist)

        for d in valid_moves[typ]:
            new_node = tuple(map(lambda x, y: x + y, node, d))
            if (
                0 <= new_node[0] < len(grid[0])
                and 0 <= new_node[1] < len(grid)
                and new_node not in visited
            ):
                q.append((new_node, grid[new_node[1]][new_node[0]], dist + 1))
            visited[node] = typ

    f = open("output.txt", "w")
    for y in range(len(grid)):
        new_line = ""
        for x in range(len(grid[0])):
            if (y, x) in visited:
                new_line += visited[(y, x)]
            else:
                new_line += "⠀"
        f.write(f"{new_line}\n")

    f.close()
    return max_dist


print(part_one())

aoc_helper.lazy_test(day=10, year=2023, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    ...


aoc_helper.lazy_test(day=10, year=2023, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=10, year=2023, solution=part_one, data=data)
aoc_helper.lazy_submit(day=10, year=2023, solution=part_two, data=data)
