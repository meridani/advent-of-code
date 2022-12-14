from copy import deepcopy
from dataclasses import dataclass
from typing import Set
import aoc_helper
from aoc_helper import (fetch)


ROCK = "█"
SAND = "░"
SAND_INPUT = "║"
AIR = " "


@dataclass
class Point:
    x: int
    y: int

    def __hash__(self) -> int:
        return hash((self.x, self.y))
    
    def __add__(self, p):
        return Point(self.x+p.x, self.y+p.y)


rocks: set[Point] = set()
sands: set[Point] = set()
sand_source = Point(500, 0)
moves = (Point(0, 1), Point(-1, 1), Point(1, 1))
min_y: int = None
min_x: int = None
max_x = 0
max_y = 0


def print_rocks():
    global rocks, sands
    print()
    for y in range(min_y, max_y+2):
        for x in range(min_x, max_x+1):
            p = Point(x,y)
            if p in rocks:
                print(ROCK, end="")
            elif p in sands:
                print(SAND, end="")
            elif p == (500, 0):
                print(SAND_INPUT, end="")
            else:
                print(AIR, end="")
        print()


def parse_raw(raw: str):
    global rocks, max_x, max_y, min_y, min_x
    for line in raw.splitlines():
        points = [p.split(",") for p in line.split(" -> ")]

        window_size = 2
        for i in range(len(points)-window_size+1):

            p1 = Point(*map(int, points[i]))
            p2 = Point(*map(int, points[i+1]))
            if min_y == None:
                min_y = min(p1.y, p2.y, 0)
            if min_x == None:
                min_x = min(p1.x, p2.x, 500)

            if p1.x == p2.x:
                for y in range(min(p1.y, p2.y), max(p1.y, p2.y)+1):
                    rocks.add(Point(p1.x, y))
                    max_y = max(max_y, y)
                    min_y = min(min_y, y)
                max_x = max(max_x, p1.x)
                min_x = min(min_x, p1.x)

            elif p1.y == p2.y:
                for x in range(min(p1.x, p2.x), max(p1.x, p2.x)+1):
                    rocks.add(Point(x, p1.y))
                    max_x = max(max_x, x)
                    min_x = min(min_x, x)
                max_y = max(max_y, p1.y)
                min_y = min(min_y, p1.y)
            else:
                print("wat")


def part_one():
    global sands

    sums = 0

    abyss = False
    while not abyss:
        new_sand = deepcopy(sand_source)
        while True:
            is_rock_down = any(rock.x == new_sand.x and rock.y >=
                               new_sand.y for rock in rocks)
            if not is_rock_down:
                abyss = True
                break

            if new_sand + moves[0] not in rocks and new_sand + moves[0] not in sands :
                new_sand += moves[0]
                continue
            if new_sand + moves[1] not in rocks and new_sand + moves[1] not in sands :
                new_sand += moves[1]
                continue
            if new_sand + moves[2] not in rocks and new_sand + moves[2] not in sands :
                new_sand += moves[2]
                continue
                
            sands.add(new_sand)
            sums += 1
            # print_rocks()
            break

    print(sums)
    return sums

def part_two():
    global sands, rocks, min_x, min_y, max_x, max_y

    sands = set()

    sums = 0

    done = False
    while not done:
        new_sand = deepcopy(sand_source)
        while not done:
            if new_sand.y-1 < max_y:
                if new_sand + moves[0] not in rocks and new_sand + moves[0] not in sands :
                    new_sand += moves[0]
                    continue
                if new_sand + moves[1] not in rocks and new_sand + moves[1] not in sands :
                    new_sand += moves[1]
                    continue
                if new_sand + moves[2] not in rocks and new_sand + moves[2] not in sands :
                    new_sand += moves[2]
                    continue
            if new_sand.y == sand_source.y:
                done = True
            sands.add(new_sand)
            min_x = min(min_x, new_sand.x)
            max_x = max(max_x, new_sand.x)
            sums += 1
            break

    print(sums)
    return sums



def test_ex1():
    raw = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""
    global data
    data = parse_raw(raw)
    assert (part_one() == 24)
    print_rocks()
    p2 = part_two()
    print_rocks()
    assert (p2 == 93)

if __name__ == "__main__":
    raw = aoc_helper.fetch(14, 2022)
    data = parse_raw(raw)
    part_one()
    part_two()
    try:
        aoc_helper.lazy_submit(day=14, year=2022, solution=part_one, data=None)
        aoc_helper.lazy_submit(day=14, year=2022, solution=part_two)
    except Exception as err:
        print("Can't upload to AoC", err)
