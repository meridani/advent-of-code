import datetime
import importlib
import os
import sys
from rich import print

# Add the current directory to the system path
sys.path.append(os.path.dirname(__file__))


def run_parts(day_module):
    module = importlib.import_module(day_module)
    raw = module.aoc_helper.fetch(module.DAY, 2024)

    print("Running day", module.DAY)

    parsed = module.parse_raw(raw)
    part1 = module.part_one(parsed)
    print(f"Part 1 answer: {part1}")

    parsed = module.parse_raw2(raw)
    part2 = module.part_two(parsed)
    print(f"Part 2 answer: {part2}")

    print("")


if __name__ == "__main__":
    now = datetime.datetime.now()
    YEAR = now.year
    DAY = now.day
    until = 1
    if YEAR <= 2024:
        until = DAY
    for day in range(1, until + 1):
        filename = f"day_{day:02}.py"
        if filename in os.listdir(os.path.dirname(__file__)):
            day_module = filename[:-3]
            run_parts(day_module)
