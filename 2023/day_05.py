from collections import defaultdict, deque
from typing import TYPE_CHECKING
from itertools import count

import aoc_helper
from aoc_helper import (
    Grid,
    PrioQueue,
    SparseGrid,
    decode_text,
    extract_ints,
    extract_iranges,
    extract_ranges,
    extract_uints,
    frange,
    irange,
    iter,
    list,
    map,
    range,
    search,
    tail_call,
)

raw = aoc_helper.fetch(5, 2023)

seeds = []

seedsoil = []
soilfertilizer =[]
fertilizerwater = []
waterlight=[]
lighttemp=[]
temphum=[]
humloc=[]


def parse_raw(raw: str):
    global seeds
    global seedsoil 
    global soilfertilizer 
    global fertilizerwater 
    global waterlight
    global lighttemp
    global temphum
    global humloc
    seeds = []
    seedsoil = []
    soilfertilizer =[]
    fertilizerwater = []
    waterlight=[]
    lighttemp=[]
    temphum=[]
    humloc=[]

    current = None
    for line in raw.splitlines():
        if line.startswith("seeds:"):
            seeds.extend(extract_uints(line))
            continue
        if line.startswith("seed-to"):
            current = seedsoil
            continue
        elif line.startswith("soil-to"):
            current = soilfertilizer
            continue
        elif line.startswith("fertilizer-to"):
            current = fertilizerwater
            continue
        elif line.startswith("water-to"):
            current = waterlight
            continue
        elif line.startswith("light-to"):
            current = lighttemp
            continue
        elif line.startswith("temperature-to"):
            current = temphum
            continue
        elif line.startswith("humidity-to"):
            current = humloc
            continue
        elif line == "":
            continue

        nums = extract_uints(line)
        current.append(tuple(nums))

    return 0


data = parse_raw(raw)

def in_map(_map:list, val:int)->int:
    for dest, src, length in _map:
        if src <= val < src+length:
            return dest + (val-src)
    return val

def not_in_map(_map:list, val:int)->int:
    for dest, src, length in _map:
        if dest <= val < dest +length:
            return src+(val-dest)
    return val

# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    
    min_val = []
    for seed in seeds:
        val = in_map(seedsoil, seed)
        val = in_map(soilfertilizer, val)
        val = in_map(fertilizerwater, val)
        val = in_map(waterlight, val)
        val = in_map(lighttemp, val)
        val = in_map(temphum, val)
        val = in_map(humloc, val)
        min_val.append(val)

    return min(min_val)

# aoc_helper.lazy_test(day=5, year=2023, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    for num in count():
        seed = not_in_map(humloc, num)
        seed = not_in_map(temphum, seed)
        seed = not_in_map(lighttemp, seed)
        seed = not_in_map(waterlight, seed)
        seed = not_in_map(fertilizerwater, seed)
        seed = not_in_map(soilfertilizer, seed)
        seed = not_in_map(seedsoil, seed)
        # Lassan, de büszkén :D
        for start, length in zip(seeds[::2], seeds[1::2]):
            if start <= seed < start+length:
                return num
                
    return 0


# aoc_helper.lazy_test(day=5, year=2023, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=5, year=2023, solution=part_one, data=data)
aoc_helper.lazy_submit(day=5, year=2023, solution=part_two, data=data)
