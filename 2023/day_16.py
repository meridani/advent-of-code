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

raw = aoc_helper.fetch(16, 2023)

DIRECTION = {
    "NORTH": (-1, 0),
    "EAST": (0, 1),
    "SOUTH": (1, 0),
    "WEST": (0, -1),
}


def parse_raw(raw: str):
    return raw.splitlines()


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    visited = defaultdict()
    beams = set()
    q = deque()
    start = (0, 0, DIRECTION["EAST"])
    q.append(start)

    while q:
        r, c, d = q.pop()
        if (r, c, d) in visited:
            continue
        visited[(r, c, d)] = True
        beams.add((r, c))
        match data[r][c]:
            case "\\" if d == DIRECTION["EAST"]:
                new_d = [DIRECTION["SOUTH"]]
            case "\\" if d == DIRECTION["WEST"]:
                new_d = [DIRECTION["NORTH"]]
            case "\\" if d == DIRECTION["NORTH"]:
                new_d = [DIRECTION["WEST"]]
            case "\\" if d == DIRECTION["SOUTH"]:
                new_d = [DIRECTION["EAST"]]

            case "/" if d == DIRECTION["EAST"]:
                new_d = [DIRECTION["NORTH"]]
            case "/" if d == DIRECTION["WEST"]:
                new_d = [DIRECTION["SOUTH"]]
            case "/" if d == DIRECTION["NORTH"]:
                new_d = [DIRECTION["EAST"]]
            case "/" if d == DIRECTION["SOUTH"]:
                new_d = [DIRECTION["WEST"]]

            case "-" if d in (DIRECTION["NORTH"], DIRECTION["SOUTH"]):
                new_d = [DIRECTION["EAST"], DIRECTION["WEST"]]

            case "|" if d in (DIRECTION["EAST"], DIRECTION["WEST"]):
                new_d = [DIRECTION["SOUTH"], DIRECTION["NORTH"]]

            case _:
                new_d = [d]
        for nd in new_d:
            dr, dc = nd

            if 0 <= r + dr < len(data) and 0 <= c + dc < len(data[0]):
                q.append((r + dr, c + dc, nd))

        # for nr, row in enumerate(data):
        #     for nc, col in enumerate(row):
        #         for vr, vc, _ in visited:
        #             if nr == vr and nc == vc:
        #                 print("#", end="")
        #                 break
        #         else:
        #             print(".", end="")
        #     print(" ", end="")
        #     for _, col in enumerate(row):
        #         print(col, end="")
        #     print()
        # print()
    return len(beams)


print(part_one())

aoc_helper.lazy_test(day=16, year=2023, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    starts = []
    for r in range(len(data) - 1):
        starts.append((r, 0, DIRECTION["EAST"]))
        starts.append((r, len(data[0]) - 1, DIRECTION["WEST"]))

    for c in range(len(data[0]) - 1):
        starts.append((0, c, DIRECTION["SOUTH"]))
        starts.append((len(data) - 1, c, DIRECTION["NORTH"]))

    mostest = 0
    for start in starts:
        visited = defaultdict()
        beams = set()
        q = deque()
        q.append(start)
        while q:
            r, c, d = q.pop()
            if (r, c, d) in visited:
                continue
            visited[(r, c, d)] = True
            beams.add((r, c))
            match data[r][c]:
                case "\\" if d == DIRECTION["EAST"]:
                    new_d = [DIRECTION["SOUTH"]]
                case "\\" if d == DIRECTION["WEST"]:
                    new_d = [DIRECTION["NORTH"]]
                case "\\" if d == DIRECTION["NORTH"]:
                    new_d = [DIRECTION["WEST"]]
                case "\\" if d == DIRECTION["SOUTH"]:
                    new_d = [DIRECTION["EAST"]]

                case "/" if d == DIRECTION["EAST"]:
                    new_d = [DIRECTION["NORTH"]]
                case "/" if d == DIRECTION["WEST"]:
                    new_d = [DIRECTION["SOUTH"]]
                case "/" if d == DIRECTION["NORTH"]:
                    new_d = [DIRECTION["EAST"]]
                case "/" if d == DIRECTION["SOUTH"]:
                    new_d = [DIRECTION["WEST"]]

                case "-" if d in (DIRECTION["NORTH"], DIRECTION["SOUTH"]):
                    new_d = [DIRECTION["EAST"], DIRECTION["WEST"]]

                case "|" if d in (DIRECTION["EAST"], DIRECTION["WEST"]):
                    new_d = [DIRECTION["SOUTH"], DIRECTION["NORTH"]]

                case _:
                    new_d = [d]
            for nd in new_d:
                dr, dc = nd

                if 0 <= r + dr < len(data) and 0 <= c + dc < len(data[0]):
                    q.append((r + dr, c + dc, nd))

            # for nr, row in enumerate(data):
            #     for nc, col in enumerate(row):
            #         for vr, vc, _ in visited:
            #             if nr == vr and nc == vc:
            #                 print("#", end="")
            #                 break
            #         else:
            #             print(".", end="")
            #     print(" ", end="")
            #     for _, col in enumerate(row):
            #         print(col, end="")
            #     print()
            # print()
        mostest = max(mostest, len(beams))
    return mostest


aoc_helper.lazy_test(day=16, year=2023, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=16, year=2023, solution=part_one, data=data)
aoc_helper.lazy_submit(day=16, year=2023, solution=part_two, data=data)
