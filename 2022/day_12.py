import collections
import aoc_helper
from aoc_helper import (Grid, PrioQueue, decode_text, extract_ints, frange,
                        irange, iter, list, map, range, tail_call)

grid: list
start: int
end: int
starts: list = []

def parse_raw(raw):
    global grid, start, end, starts
    grid = [list(line) for line in raw.splitlines()]
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == "S":
                start = (i,j)
                starts.append((i,j))
                grid[i][j] = 'a'
            elif col == "E":
                end = (i,j)
                grid[i][j] = 'z'
            elif col == "a":
                starts.append((i,j))

def bfs(grid, start, end):
    q = collections.deque()
    q.append((start, 0))
    seen = set()
    while q:
        pos, dist = q.popleft()
        if pos == end:
            return dist
        if pos in seen:
            continue
        seen.add(pos)
        x, y = pos
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            if (
                0 <= x + dx < len(grid)
                and 0 <= y + dy < len(grid[0])
                and ord(grid[x + dx][y + dy]) - ord(grid[x][y]) <= 1
            ):
                q.append(((x + dx, y + dy), dist + 1))
    return float("inf")

def part_one():
    global start, end, grid
    return bfs(grid, start, end)


def part_two():
    global starts, start, end, grid
    return sorted([bfs(grid, item, end) for item in starts])[0]

def test_ex1():
    raw="""Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""
    global data
    data = parse_raw(raw)
    assert(part_one()==31)
    assert(part_two()==29)

if __name__ == "__main__":
    raw = aoc_helper.fetch(12, 2022)
    data = parse_raw(raw)
    try:
        aoc_helper.lazy_submit(day=12, year=2022, solution=part_one)
        aoc_helper.lazy_submit(day=12, year=2022, solution=part_two)
    except Exception as err:
        print("Can't upload to AoC", err)