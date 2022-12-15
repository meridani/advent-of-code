from __future__ import annotations
from dataclasses import dataclass
import re
import aoc_helper
from aoc_helper import (Grid, PrioQueue, decode_text, extract_ints, frange,
                        irange, iter, list, map, range, tail_call)

from day_14 import Point


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
        


def extract_ints(raw: str) -> "list[int]":
    return list(map(int, re.findall(r"((?:-|\+)?\d+)", raw)))


def parse_raw(raw: str):
    global sensors, beacons
    for line in raw.splitlines():
        ints = extract_ints(line)
        sensors.append(Point(ints[0], ints[1]))
        beacons.append(Point(ints[2], ints[3]))

def part_one():
    global sensors, beacons, manhattans

    for sensor, beacon in zip(sensors, beacons):
        dist = sensor.manhattan(beacon)
        closest = Point(sensor.x, row_in_question).manhattan(sensor)
        if dist >= closest:
            # length = 1 + abs(dist - closest) * 2
            length = abs(dist - abs(sensor.y-row_in_question))
            # xs = [Point(x, row_in_question) for x in range(sensor.x-(length//2), sensor.x + (length//2) + 1)]
            xs = [Point(x, row_in_question) for x in range(sensor.x-length, sensor.x + length + 1)]
            # print(xs)
            ans.update(xs)
            
    ans.difference_update(sensors)
    ans.difference_update(beacons)
    
    return len(ans)
        # manhattans.append(sensor.manhattan(beacon))


def part_two():
    ...

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
    global data, row_in_question
    row_in_question = 10
    data = parse_raw(raw)
    assert(part_one()==26)
    assert(part_two()==0)

if __name__ == "__main__":
    raw = aoc_helper.fetch(15, 2022)
    data = parse_raw(raw)
    print(part_one())
    try:
        aoc_helper.lazy_submit(day=15, year=2022, solution=part_one)
        aoc_helper.lazy_submit(day=15, year=2022, solution=part_two)
    except Exception as err:
        print("Can't upload to AoC", err)