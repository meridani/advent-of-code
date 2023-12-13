import aoc_helper
from aoc_helper import (Grid, PrioQueue, decode_text, extract_ints, frange,
                        irange, iter, list, map, range, tail_call)


def parse_raw(raw):
    return raw

def part_one():
    ...


def part_two():
    ...

def test_ex1():
    raw="""Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""
    global data
    data = parse_raw(raw)
    assert(part_one()==1651)
    assert(part_two()==0)

if __name__ == "__main__":
    raw = aoc_helper.fetch(16, 2022)
    data = parse_raw(raw)
    try:
        aoc_helper.lazy_submit(day=16, year=2022, solution=part_one)
        aoc_helper.lazy_submit(day=16, year=2022, solution=part_two)
    except Exception as err:
        print("Can't upload to AoC", err)