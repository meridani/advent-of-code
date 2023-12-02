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

raw = aoc_helper.fetch(2, 2023)

RED = 12
GREEN = 13
BLUE = 14


class Game:
    _id = 0
    _possible = False
    _draws = []
    _r = 0
    _b = 0
    _g = 0

    def __init__(self) -> None:
        self._id = 0
        self._possible = True
        self._r = 0
        self._b = 0
        self._g = 0
        self._draws = []

    def check_valid(self):
        for d in self._draws:
            match d[1].strip():
                case "red":
                    self._r = max(self._r, d[0])
                    if d[0] > RED:
                        self._possible = False
                case "blue":
                    self._b = max(self._b, d[0])
                    if d[0] > BLUE:
                        self._possible = False
                case "green":
                    self._g = max(self._g, d[0])
                    if d[0] > GREEN:
                        self._possible = False
        if not self._possible:
            return False

        return True


def parse_raw(raw: str) -> list[Game]:
    game_list = []
    for line in raw.splitlines():
        g = Game()
        parts = line.split(":")
        g._id = extract_uints(parts[0])[0]
        games = parts[1].split(";")
        for game in games:
            draws = game.split(",")
            for draw in draws:
                p = draw.strip().split(" ")
                g._draws.append((int(p[0]), p[1]))
        g.check_valid()
        game_list.append(g)
    return game_list


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    sums = 0
    for g in data:
        if g._possible:
            sums += g._id
    return sums


aoc_helper.lazy_test(day=2, year=2023, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    sums = 0

    for game in data:
        power = game._r * game._g * game._b
        sums += power
    return sums


aoc_helper.lazy_test(day=2, year=2023, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=2, year=2023, solution=part_one, data=data)
aoc_helper.lazy_submit(day=2, year=2023, solution=part_two, data=data)
