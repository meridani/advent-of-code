import aoc_helper
from aoc_helper import (Grid, PrioQueue, decode_text, extract_ints, frange,
                        irange, iter, list, map, range, tail_call)

raw = aoc_helper.fetch(6, 2022)

def parse_raw():
    return ''.join(raw.splitlines())

data: str = parse_raw()

def get_first_distinct(l, window_size=4):
    for i in range(len(data)-window_size):
        if len(set(data[i:i+window_size])) == window_size:
            return i+window_size

def part_one():
    return get_first_distinct(data)


def part_two():
    return get_first_distinct(data,14)


def test_ex1():
    global data
    global raw
    raw = """bvwbjplbgvbhsrlpgdmjqwftvncz"""
    data = parse_raw()
    assert (part_one() == 5)
    raw = """nppdvjthqldpwncqszvftbrmjlhg"""
    data = parse_raw()
    assert (part_one() == 6)
    raw = """nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"""
    data = parse_raw()
    assert (part_one() == 10)
    raw = """zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"""
    data = parse_raw()
    assert (part_one() == 11)

def test_ex2():
    global data
    global raw
    raw = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""
    data = parse_raw()
    assert (part_one() == 19)
    raw = """bvwbjplbgvbhsrlpgdmjqwftvncz"""
    data = parse_raw()
    assert (part_one() == 23)
    raw = """nppdvjthqldpwncqszvftbrmjlhg"""
    data = parse_raw()
    assert (part_one() == 23)
    raw = """nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"""
    data = parse_raw()
    assert (part_one() == 29)
    raw = """zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"""
    data = parse_raw()
    assert (part_one() == 26)

if __name__ == "__main__":
    # test_ex1()
    print(part_one())
    print(part_two())
    aoc_helper.lazy_submit(day=6, year=2022, solution=part_one)
    aoc_helper.lazy_submit(day=6, year=2022, solution=part_two)
