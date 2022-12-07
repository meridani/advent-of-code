import aoc_helper
from aoc_helper import range


def parse_raw(raw):
    return ''.join(raw.splitlines())

data: str
distinct: int

def get_first_distinct(window_size=4):
    for i in range(len(data)-window_size):
        if len(set(data[i:i+window_size])) == window_size:
            return i+window_size

def part_one():
    return get_first_distinct()


def part_two():
    return get_first_distinct(distinct)


def test_ex1():
    global data
    raw = """bvwbjplbgvbhsrlpgdmjqwftvncz"""
    data = parse_raw(raw)
    assert (part_one() == 5)
    raw = """nppdvjthqldpwncqszvftbrmjlhg"""
    data = parse_raw(raw)
    assert (part_one() == 6)
    raw = """nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"""
    data = parse_raw(raw)
    assert (part_one() == 10)
    raw = """zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"""
    data = parse_raw(raw)
    assert (part_one() == 11)

def test_ex2():
    global data
    global distinct
    distinct = 14
    raw = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""
    data = parse_raw(raw)
    assert (part_two() == 19)
    raw = """bvwbjplbgvbhsrlpgdmjqwftvncz"""
    data = parse_raw(raw)
    assert (part_two() == 23)
    raw = """nppdvjthqldpwncqszvftbrmjlhg"""
    data = parse_raw(raw)
    assert (part_two() == 23)
    raw = """nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"""
    data = parse_raw(raw)
    assert (part_two() == 29)
    raw = """zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"""
    data = parse_raw(raw)
    assert (part_two() == 26)

if __name__ == "__main__":
    try:
        raw = aoc_helper.fetch(6, 2022)
        data = parse_raw(raw)
        aoc_helper.lazy_submit(day=6, year=2022, solution=part_one)
        aoc_helper.lazy_submit(day=6, year=2022, solution=part_two)
    except:
        print("Can't upload to AoC")