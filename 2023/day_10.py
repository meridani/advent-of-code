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
    for r, line in enumerate(raw.splitlines()):
        if "S" in line:
            start = (r, line.index("S"))
        data.append(list(line))

    return data, start


data = parse_raw(raw)

NORTH = (-1, 0)
EAST = (0, 1)
SOUTH = (1, 0)
WEST = (0, -1)
valid_moves = {
    # "X": [EAST, WEST],  # Manually looked at the input file...
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
    grid[start[0]][start[1]] = "-"
    q.append((start, "-", 0))
    while q:
        node, typ, dist = q.popleft()
        max_dist = max(dist, max_dist)

        for d in valid_moves[typ]:
            new_node = tuple(map(lambda x, y: x + y, node, d))
            if (
                0 <= new_node[0] < len(grid)
                and 0 <= new_node[1] < len(grid[0])
                and new_node not in visited
            ):
                q.append((new_node, grid[new_node[0]][new_node[1]], dist + 1))
        visited[node] = typ

    return max_dist


print(part_one())

aoc_helper.lazy_test(day=10, year=2023, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    visited = {}
    start = data[1]
    grid = data[0]
    q = deque()
    max_dist = -inf
    grid[start[0]][start[1]] = "-"
    q.append((start, "-", 0))
    while q:
        node, typ, dist = q.popleft()
        max_dist = max(dist, max_dist)

        for d in valid_moves[typ]:
            new_node = tuple(map(lambda x, y: x + y, node, d))
            if (
                0 <= new_node[0] < len(grid)
                and 0 <= new_node[1] < len(grid[0])
                and new_node not in visited
            ):
                q.append((new_node, grid[new_node[0]][new_node[1]], dist + 1))
        visited[node] = typ

    insides = set()
    for r, line in enumerate(grid):
        inside = False
        for c, pipe in enumerate(line):
            if (r, c) in visited:
                if pipe in "|F7":
                    inside = not inside
            else:
                if inside:
                    insides.add((r, c))

    return len(insides)


# def test():
#     raw = r"...........\
# .S-------7.\
# .|F-----7|.\
# .||.....||.\
# .||.....||.\
# .|L-7.F-J|.\
# .|..|.|..|.\
# .L--J.L--J.\
# ..........."
#     data = parse_raw(raw)
#     print(part_two(data))


# test()
print(part_two())

aoc_helper.lazy_test(day=10, year=2023, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=10, year=2023, solution=part_one, data=data)
aoc_helper.lazy_submit(day=10, year=2023, solution=part_two, data=data)
