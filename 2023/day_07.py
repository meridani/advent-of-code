from collections import defaultdict, deque, Counter
from typing import TYPE_CHECKING

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

raw = aoc_helper.fetch(7, 2023)

# class Hand:
#     cards = []
#     bid = 0
#     rank = 0
#     strength = 0

#     def __init__(self, cards, bid, rank=None, strength=None) -> None:
#         self.cards = cards
#         self.bid = bid

#         c = Counter(cards)

#         if strength is not None:
#             self.strength = strength
#         else:
#             self.strength=tuple(sorted(c.values()))
        
#         if rank is not None:
#             self.rank = rank
#         else:
#             match sorted(c.values()):
#                 case [5]:
#                     self.rank = 6
#                 case [1,4]:
#                     self.rank = 5
#                 case [2,3]:
#                     self.rank = 4
#                 case [1,1,3]:
#                     self.rank = 3
#                 case [1,2,2]:
#                     self.rank = 2
#                 case [1,1,1,2]:
#                     self.rank = 1
#                 case [1,1,1,1,1]:
#                     self.rank = 0
        

def parse_raw(raw: str):
    hands = []

    for line in raw.splitlines():
        hand , bid = line.split()
        # hand = list(hand)
        bid = int(bid)

        # for i in range(len(hand)):
        #     match hand[i]:
        #         case 'T':
        #             hand[i] = 10
        #         case 'J':
        #             hand[i] = 11
        #         case 'Q':
        #             hand[i] = 12
        #         case 'K':
        #             hand[i] = 13
        #         case 'A':
        #             hand[i] = 14
        #         case _:
        #             hand[i] = int(hand[i])

        # hand = ["__23456789TJQKA".index(i) for i in hand]

        # cards = Counter(hand)
        hands.append((hand, bid))


    return hands


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    games = []
    for hand in data:
        new_hand = ['23456789TJQKA'.index(i) for i in hand[0]]
        c = Counter(hand[0])
        p = tuple(sorted(c.values()))
        t = [(1,1,1,1,1),(1,1,1,2),(1,2,2),(1,1,3),(2,3),(1,4),(5,)].index(p)
            
        games.append((t, list(map(int,new_hand)), hand[1]))
    
    score = 0
    games = sorted(games)
    for i,(_,_,b) in enumerate(games):
        score+=i*b+b
    return score



aoc_helper.lazy_test(day=7, year=2023, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    games = []
    for hand in data:
        h2 = ['J23456789TXQKA'.index(i) for i in hand[0]]
        ts = []
        for r in '23456789TQKA':
            c = Counter(hand[0].replace('J', r))
            p = tuple(sorted(c.values()))
            t = [(1,1,1,1,1),(1,1,1,2),(1,2,2),(1,1,3),(2,3),(1,4),(5,)].index(p)
            ts.append(t)
            
        games.append(((max(ts), *h2), hand[1]))
    
    score = 0
    games = sorted(games)
    for i,(_,b) in enumerate(games):
        score+=i*b+b
    return score


aoc_helper.lazy_test(day=7, year=2023, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=7, year=2023, solution=part_one, data=data)
aoc_helper.lazy_submit(day=7, year=2023, solution=part_two, data=data)
