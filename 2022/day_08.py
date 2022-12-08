import aoc_helper
from aoc_helper import (Grid, PrioQueue, decode_text, extract_ints, frange,
                        irange, iter, list, map, range, tail_call)

score:int

def parse_raw(raw):
    return [[int(item) for item in line.strip()] for line in raw.splitlines()]


def part_one():
    visible = 0
    for i,row in enumerate(data):
        for j,_ in enumerate(row):
            tree = data[i][j]

            top = list(reversed([tree > row[j] for row in data[:i]]))
            down = [tree > row[j] for row in data[i+1:]]
            left =  list(reversed([tree > col for col in data[i][:j]]))
            right = [tree > col for col in data[i][j+1:]]

            top_d = top.index(False) + 1 if (False in top) else len(top)
            down_d = down.index(False) + 1 if (False in down) else len(down)
            left_d = left.index(False) + 1 if (False in left) else len(left)
            right_d = right.index(False) + 1 if (False in right) else len(right)

            if any([all(top), all(down), all(left), all(right)]):
                visible += 1
                
            current = top_d * down_d * left_d * right_d

            global score
            if current > score:
                score = current

    return visible


def part_two():
    global score
    return score


def test_ex1():
    raw = """30373
25512
65332
33549
35390"""
    global data
    data = parse_raw(raw)
    assert (part_one() == 21)
    assert (part_two() == 8)


if __name__ == "__main__":
    raw = aoc_helper.fetch(8, 2022)
    data = parse_raw(raw)
    try:
        aoc_helper.lazy_submit(day=8, year=2022, solution=part_one)
        aoc_helper.lazy_submit(day=8, year=2022, solution=part_two)
    except:
        print("Can't upload to AoC")

