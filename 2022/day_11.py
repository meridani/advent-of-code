from copy import deepcopy
from dataclasses import dataclass
from math import prod
import aoc_helper
from aoc_helper import (Grid, PrioQueue, decode_text, extract_ints, frange,
                        irange, iter, list, map, range, tail_call)


@dataclass
class Monkey:
    name: str
    items: list[int]
    throw_true: int
    throw_false: int
    operation: str
    divisor: int
    inspected: int = 0

    def catch(self, item, modulo = 0):
        if modulo == 0:
            self.items.append(item)
        else:
            self.items.append(item % modulo)

    def turn(self, worry = True) -> list:
        l = []
        for item in self.items:
            self.inspected+= 1
            item = eval(self.operation, {"old": item})
            item = item //3 if worry else item
            if item % self.divisor == 0:
                l.append([self.throw_true, item])
            else:
                l.append([self.throw_false, item])
        self.items = []
        return l


monkeys: list[Monkey] = []


def parse_raw(raw: str) -> list[Monkey]:
    global monkeys
    newMonkey: Monkey

    for line in raw.splitlines():
        if line.startswith("Monkey"):
            name = line.strip(":").split()[-1]
        elif line.strip().startswith("Starting"):
            items = list(map(int, line.split(":")[1].split(",")))
        elif line.strip().startswith("Operation"):
            operation = line.split("=")[1]
        elif line.strip().startswith("Test"):
            divisor = int(line.split()[-1])
        elif "true" in line.strip():
            t = int(line.split()[-1])
        elif "false" in line.strip():
            f = int(line.split()[-1])
        elif line.strip() == "":
            newMonkey = Monkey(name=name, items=items, throw_true=t, throw_false=f, operation=operation, divisor=divisor)
            monkeys.append(newMonkey)
    else:
        newMonkey = Monkey(name=name, items=items, throw_true=t, throw_false=f, operation=operation, divisor=divisor)
        monkeys.append(newMonkey)

def play(r:int, worry=True):
    global monkeys
    m = deepcopy(monkeys)

    # https://en.wikipedia.org/wiki/Chinese_remainder_theorem
    modulo = prod([monkey.divisor for monkey in m])

    for _ in range(r):
        for monkey in m:
            throws = monkey.turn(worry)
            for throw in throws:
                what = throw[1]
                to = throw[0]
                m[to].catch(what, modulo)

    inspects = list([inspects.inspected for inspects in m]).sorted(reverse=True)[:2]
    print(inspects, prod(inspects))
    return prod(inspects)

def part_one():
    return play(20)


def part_two():
    return play(10000, False)


def test_ex1():
    raw = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""
    parse_raw(raw)
    assert (part_one() == 10605)
    assert (part_two() == 2713310158)


if __name__ == "__main__":
    raw = aoc_helper.fetch(11, 2022)
    data = parse_raw(raw)
    try:
        aoc_helper.lazy_submit(day=11, year=2022, solution=part_one)
        aoc_helper.lazy_submit(day=11, year=2022, solution=part_two)
    except Exception as err:
        print("Can't upload to AoC", err)
