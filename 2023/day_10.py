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
    q.append((start, "-", 0))
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
    q.append((start, "-", 0))
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

    ins = 0
    inside = False
    enter = ""
    for r, line in enumerate(grid):
        for c, pipe in enumerate(line):
            match pipe:
                case _ if (c, r) not in visited and not inside:
                    continue
                case _ if (c, r) not in visited and inside:
                    ins += 1
                case "-":
                    ins += 1
                case "F" | "|" | "L" if not inside:
                    ins += 1
                    inside = True
                    enter = pipe
                case "|":
                    if inside:
                        inside = False
                case "L":
                    ins += 1
                case "J":
                    ins += 1
                    if enter in "L|F":
                        inside = False
                        enter = ""
                case "7":
                    ins += 1
                    if enter in "L|F":
                        inside = False
                        enter = ""
                case "F":
                    ins += 1
                # case "|" if inside:
                #     ins += 1
                #     inside = False
                #     enter = ""
                # case "F" if enter in "L":
                #     ins += 1
                # case "7" if enter in "L":
                #     ins += 1
                # case "7" if enter in "F|" and inside:
                #     ins += 1
                #     inside = False
                #     enter = ""
                # case "J" if enter in "F":
                #     ins += 1
                # case "J" if enter in "|L" and inside:
                #     ins += 1
                #     inside = False
                #     enter = ""
                case _:
                    print((r, c), pipe, inside, enter)
    return ins - len(visited)


print(part_two())

# aoc_helper.lazy_test(day=10, year=2023, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=10, year=2023, solution=part_one, data=data)
# aoc_helper.lazy_submit(day=10, year=2023, solution=part_two, data=data)
