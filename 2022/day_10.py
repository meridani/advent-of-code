from enum import Enum
import aoc_helper
from aoc_helper import (Grid, PrioQueue, decode_text, extract_ints, frange,
                        irange, iter, list, map, range, tail_call)

WIDTH = 40
HEIGHT = 6
# PIXEL_DARK = " "
# PIXEL_BRIGHT = "█"
PIXEL_DARK = "."
PIXEL_BRIGHT = "#"

def parse_raw(raw):
    return [INSTRUCTION(*item.split()) for item in raw.splitlines()]


class INSTRUCTION:
    opcode: str
    data1: int
    data2: int

    def __init__(self, opcode: str, data1: str = "", data2: str="") -> None:
        self.opcode = opcode
        self.data1 = int(data1) if data1 else 0
        self.data2 = int(data2) if data2 else 0


class DEVICE:
    cycle: int
    X: int
    signalStrength: int
    crt = []

    def __repr__(self) -> str:
        return self.signalStrength

    def __str__(self) -> str:
        return str(self.signalStrength)

    def __int__(self):
        return self.signalStrength

    def __init__(self) -> None:
        self.X = 1
        self.cycle = 0
        self.signalStrength = 0
        self.crt = list(PIXEL_DARK * (WIDTH*HEIGHT))
        
    def execute(self, instruction: INSTRUCTION):
     match instruction.opcode:
            case "noop":
                self.crt_update()
                self.cycle += 1
                if (self.cycle+20) % 40 == 0:
                    self.signalStrength += self.cycle * self.X
            case "addx":
                self.crt_update()
                self.cycle += 1
                if (self.cycle+20) % 40 == 0:
                    self.signalStrength += self.cycle * self.X
                self.crt_update()
                self.cycle += 1
                if (self.cycle+20) % 40 == 0:
                    self.signalStrength += self.cycle * self.X
                self.X += instruction.data1

    def crt_update(self):
        min = (self.X - 1) % len(self.crt)
        max = (self.X + 1) % len(self.crt)
        sprite = [min, self.X % len(self.crt), max]

        if(self.cycle % WIDTH) in sprite:
            self.crt[(self.cycle) % len(self.crt)] = PIXEL_BRIGHT

    def print_crt(self):
        print('\n'.join([''.join(self.crt[i:i + WIDTH])
                    for i in range(0, len(self.crt), WIDTH)]))
        return ('\n'.join([''.join(self.crt[i:i + WIDTH])
                    for i in range(0, len(self.crt), WIDTH)]))


def part_one():
    cpu = DEVICE()
    for instr in data:
        cpu.execute(instr)
    return int(cpu)


def part_two():
    cpu = DEVICE()
    for instr in data:
        cpu.execute(instr)
    return cpu.print_crt()

def test_ex1():
    raw = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""
    global data
    data = parse_raw(raw)
    assert (part_one() == 13140)
    assert (part_two() == """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....""")


if __name__ == "__main__":
    raw = aoc_helper.fetch(10, 2022)
    data = parse_raw(raw)
    try:
        aoc_helper.lazy_submit(day=10, year=2022, solution=part_one)
    except Exception as err:
        print("Can't upload to AoC", err)
    try:
        aoc_helper.lazy_submit(day=10, year=2022, solution=part_two)
    except Exception as err:
        print("Can't upload to AoC", err)
