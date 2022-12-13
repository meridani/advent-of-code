import json
import aoc_helper
from aoc_helper import (Grid, PrioQueue, decode_text, extract_ints, frange,
                        irange, iter, map, range, tail_call)



class Message:
    message_left: list
    message_right: list

    def __init__(self, message_left, message_right) -> None:
        self.message_left = message_left
        self.message_right = message_right 

list_messages: list[Message] = []


def check_pair(a, b):
    match (a, b):
        case int(), int(): 
            return b - a
        case int(), list(): 
            return check_pair([a], b)
        case list(), int(): 
            return check_pair(a, [b])
        case list(), list():
            for aa, bb in zip(a, b):
                if (r := check_pair(aa, bb)) != 0:
                    return r
            return len(b) - len(a)
    assert False


def parse_raw(raw):
    global list_messages
    messages = raw.split("\n\n")

    for m in messages:
        parts = m.splitlines()
        list_messages.append((json.loads(parts[0]), json.loads(parts[1])))


smallers = [0,0]
def part_one():
    global list_messages
    global smallers
    sums = 0

    for i, m in enumerate(list_messages):
        if check_pair(m[0], m[1]) > 0:
            sums += i+1
        for o in (m[0], m[1]):
            smallers[0] += 1 if check_pair(o, [[2]]) > 0 else 0
            smallers[1] += 1 if check_pair(o, [[6]]) > 0 else 0
    return sums


def part_two():
    return (smallers[0] + 1) * (smallers[1] + 2)   

def test_ex1():
    raw="""[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""
    global data
    data = parse_raw(raw)
    assert(part_one()==13)
    assert(part_two()==140)

if __name__ == "__main__":
    raw = aoc_helper.fetch(13, 2022)
    data = parse_raw(raw)
    try:
        aoc_helper.lazy_submit(day=13, year=2022, solution=part_one)
        aoc_helper.lazy_submit(day=13, year=2022, solution=part_two)
    except Exception as err:
        print("Can't upload to AoC", err)