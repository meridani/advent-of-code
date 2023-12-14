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

raw = aoc_helper.fetch(14, 2023)


def parse_raw(raw: str):
    return list([list(x) for x in raw.splitlines()])


data = parse_raw(raw)

def rotate(data):
    return [(x[::-1]) for x in list(map(aoc_helper.list, zip(*data)))]

def move(data):
    done = False
    while not done:
        done = True
        for r, line in enumerate(data[:-1]):
            for c, s in enumerate(line):
                if s == "." and data[r+1][c] == "O":
                    line[c] = "O"
                    data[r+1][c] = "."
                    done = False
    return data

def value(data):
    sums = 0
    for r, line in enumerate(data[::-1], start=1):
        for c, s in enumerate(line):
            if s == "O":
                sums += r
    return sums



# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    # rocks = [(r,c) for c in range(len(data[0])) for r in range(len(data)) if (data[r][c]=="#")]
    
    data = move(data)
    return value(data)
    


aoc_helper.lazy_test(day=14, year=2023, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    visited = {}
    runs = 1_000_000_000
    for cycle in range(runs):
        print(f"Running: {cycle}")
        k = tuple(tuple(line) for line in data)
        if k in visited:
            loop = []
            d = visited[k]
            loop.append(visited[k])
            while d != k:
                loop.append(visited[d])
                d = visited[d]
            if loop:
                break

            data = [list(l) for l in visited[k]]
            continue

        for _ in range(4):
            data = move(data)
            data = rotate(data)
        n = tuple(tuple(line) for line in data)
        visited[k]= n
        
    print(cycle, len(loop))
    data = [list(l) for l in loop[(runs-cycle)%len(loop)-1]]

    # for d in loop:
    #     print(value([list(l) for l in d]))

    return value(data)

# print(part_two())


aoc_helper.lazy_test(day=14, year=2023, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=14, year=2023, solution=part_one, data=data)
aoc_helper.lazy_submit(day=14, year=2023, solution=part_two, data=data)
