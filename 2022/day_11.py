from copy import deepcopy
from dataclasses import dataclass
import operator
from typing import Callable, NewType
import aoc_helper
from aoc_helper import (Grid, PrioQueue, decode_text, extract_ints, frange,
                        irange, iter, list, map, range, tail_call)


@dataclass
class Monkey:
    name: str
    items: list[int]
    throw_true: int
    throw_false: int
    operation: Callable[[int], int]
    operand: int
    divisor: int
    inspected: int = 0

    def catch(self, item):
        self.items.append(item)

    def turn(self, worry = True) -> list:
        l = []
        self.inspected+= len(self.items)
        for i in self.items:
            operand = self.operand if self.operand != 0 else i
            y = self.operation(i, operand)
            if worry:
                z = y//3
            else:
                z = y
            if z % self.divisor == 0:
                l.append([self.throw_true, z])
            else:
                l.append([self.throw_false, z])
        self.items = []
        return l


monkeys: list[Monkey] = []


def parse_raw(raw: str) -> list[Monkey]:
    """
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3"""
    global monkeys
    newMonkey: Monkey

    for line in raw.splitlines():
        if line.startswith("Monkey"):
            name = line.strip(":").split()[-1]
        elif line.strip().startswith("Starting"):
            items = list(map(int, line.split(":")[1].split(",")))
        elif line.strip().startswith("Operation"):
            l = line.split("=")[1].split()
            op = l[-2]
            num = l[-1]
            match op:
                case "*":
                    if num == "old":
                        operand = 0
                        # def operation(a: int): return a * a
                        operation = operator.mul
                    else:
                        n = int(num)
                        operand = n
                        # def operation(a: int): return a * n
                        operation = operator.mul

                case "+":
                    if num == "old":
                        operand = 0
                        # def operation(a): return a + a
                        operation = operator.add
                    else:
                        n = int(num)
                        operand = n
                        # def operation(a): return a + n  
                        operation = operator.add


            op = operation

        elif line.strip().startswith("Test"):
            divisor = int(line.split()[-1])
            # test = operator.mod
        elif "true" in line.strip():
            t = int(line.split()[-1])
        elif "false" in line.strip():
            f = int(line.split()[-1])
        elif line.strip() == "":
            newMonkey = Monkey(name=name, items=items, throw_true=t, throw_false=f, operation=op, divisor=divisor, operand=operand)
            monkeys.append(newMonkey)
    else:
        newMonkey = Monkey(name=name, items=items, throw_true=t, throw_false=f, operation=op, divisor=divisor, operand=operand)
        monkeys.append(newMonkey)

def part_one():
    global monkeys
    m = deepcopy(monkeys)

    for _ in range(20):
        for monkey in m:
            throws = monkey.turn()
            for throw in throws:
                m[throw[0]].catch(throw[1])

    m = [inspects.inspected for inspects in m]
    first = max(m)
    m.remove(first)
    second = max(m)
    return first * second


def part_two():
    global monkeys
    m = deepcopy(monkeys)

    for round in range(10000):
        # if round % 100 == 0:
        print(f"round: {round}")
        for monkey in m:
            throws = monkey.turn(False)
            for throw in throws:
                m[throw[0]].catch(throw[1])

    m = [inspects.inspected for inspects in m]
    first = max(m)
    m.remove(first)
    second = max(m)
    return first * second


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
