import aoc_helper
from aoc_helper import (Grid, PrioQueue, decode_text, extract_ints, frange,
                        irange, iter, list, map, range, tail_call)

data:list

def parse_raw(raw):
    return raw.splitlines()

class Point:
    x: int
    y: int 

    def __init__(self, x,y):
        self.x =  x
        self.y = y

    def __repr__(self):
        return f"x: {self.x}, y: {self.y}"

    def __hash__(self):
        return hash(repr(self))

    def step(self, dir: str):
        match dir:
            case 'R':
                self.x += 1 
            case 'L':
               self.x -= 1 
            case 'U':
                self.y += 1
            case 'D':
                self.y -= 1 
    
    def follow(self, other: 'Point'):
        dx = other.x - self.x 
        dy = other.y - self.y 
       
        if abs(dx) <= 1 and abs(dy) <= 1:
            return 

        if dx == 0:
            self.y += 1 if dy == 2 else -1 
        elif dy == 0:
            self.x += 1 if dx == 2 else -1
        else:  
            self.y += 1 if dy > 0 else -1 
            self.x += 1 if dx > 0 else -1

def solve(n: int) -> int:
    knots = [Point(0, 0) for _ in range(0, n)]
    visited = set()

    for line in data:
        dir, steps = line.split()

        for _ in range(int(steps)):
            knots[0].step(dir)

            for a, b in zip(knots, knots[1:]):
                b.follow(a) 
          
            visited.add(knots[-1])

    return len(visited)

def part_one():
    return solve(2)

def part_two():
    return solve(10)

def test_ex1():
    raw="""R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""
    global data
    data = parse_raw(raw)
    assert(part_one()==13)
    assert(part_two()==1)
    
def test_ex2():
    raw="""R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""
    global data
    data = parse_raw(raw)
    assert(part_two()==36)

if __name__ == "__main__":
    raw = aoc_helper.fetch(9, 2022)
    data = parse_raw(raw)
    try:
        aoc_helper.lazy_submit(day=9, year=2022, solution=part_one)
        aoc_helper.lazy_submit(day=9, year=2022, solution=part_two)
    except Exception as err:
        print("Can't upload to AoC", err)