from __future__ import annotations
from dataclasses import dataclass
import re
import timeit
import aoc_helper
from aoc_helper import (Grid, PrioQueue, decode_text, extract_ints, frange,
                        irange, iter, list, map, range, tail_call)

from day_14 import Point

MAX = 4_000_000

beacons: list[Point] = list()
sensors: list[Point] = list()
manhattans: list[Point] = list()
row_in_question: int = 2000000
ans: set[int] = set()

# @dataclass
# class Vector:
#     s: Point
#     e: Point

#     def union(self, v: Vector) -> Vector:
        
lines: str = ""

def extract_ints(raw: str) -> "list[int]":
    return list(map(int, re.findall(r"((?:-|\+)?\d+)", raw)))


def parse_raw(raw: str):
    global sensors, beacons, lines
    lines = raw
    for line in raw.splitlines():
        ints = extract_ints(line)
        sensors.append(Point(ints[0], ints[1]))
        beacons.append(Point(ints[2], ints[3]))

def part_one():
    global sensors, beacons, manhattans
    beacon_y = set()
    for sensor, beacon in zip(sensors, beacons):

        if beacon.y == row_in_question:
            beacon_y.add(beacon.y)

        dist = sensor.manhattan(beacon)
        manhattans.append(dist)
        closest = Point(sensor.x, row_in_question).manhattan(sensor)
        if dist >= closest:
            dist -= abs(sensor.y-row_in_question)
            xs = [x for x in range(sensor.x-dist, sensor.x + dist + 1)]
            ans.update(xs)
                
    return len(ans) - len(beacon_y)


def part_two():
    global sensors, beacons, manhattans
    y = [[] for _ in range(MAX+1)]
    for sensor, d in zip(sensors, manhattans):

        dy = 0
        while d > 0:
            left = max(0, sensor.x - d)
            right = min(MAX, sensor.x + d)
            if(sensor.y - dy >= 0):
                y[sensor.y - dy].append([left, right])
            if(sensor.y + dy <= MAX and dy):
                y[sensor.y + dy].append([left, right])
            dy += 1
            d -= 1

        for ans_y in range(MAX + 1):
            xs = y[ans_y]
            if not xs:
                continue
            xs.sort()
            
            if xs[0][0] != 0:
                ans_x = 0
                break

            last_e = xs[0][1]
            for i in range(1, len(xs)):
                if last_e >= xs[i][0] - 1:
                    last_e = max(last_e, xs[i][1])
                else:
                    break

            if last_e != MAX:
                ans_x = last_e + 1
                break
        
    return 4000000 * ans_x + ans_y


def test_ex1():
    raw="""Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""
    global data, row_in_question, MAX
    MAX = 20
    row_in_question = 10
    data = parse_raw(raw)
    assert(part_one()==26)
    assert(part_two()==56000011)

if __name__ == "__main__":
    raw = aoc_helper.fetch(15, 2022)
    data = parse_raw(raw)
    print(timeit.timeit(part_one, number= 2))
    print(timeit.timeit(part_two, number= 1))

    try:
        aoc_helper.lazy_submit(day=15, year=2022, solution=part_one)
        aoc_helper.lazy_submit(day=15, year=2022, solution=part_two)
    except Exception as err:
        print("Can't upload to AoC", err)