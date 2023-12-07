#! /usr/bin/python

import sys, re

def gametype(hand):
    jokers = sum(c == 'J' for c in hand)
    if jokers == 5: return 6
    cards = [c for c in hand if c != 'J']
    counts = {}
    for card in cards:
        counts[card] = counts.get(card, 0) + 1
    counts = sorted(counts.values())
    counts[-1] += jokers
    if counts == [5]: return 6
    if counts == [1, 4]: return 5
    if counts == [2, 3]: return 4
    if counts == [1, 1, 3]: return 3
    if counts == [1, 2, 2]: return 2
    if counts == [1, 1, 1, 2]: return 1
    return 0

def cardrank(card):
    return "J23456789TQKA".index(card)

def sortkey(hand_bid):
    hand = hand_bid[0]
    return (gametype(hand), [ cardrank(card) for card in hand ])

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

hands = []
with open(filename) as f:
    for line in f:
        hand, bid = line.split()
        hands.append((hand, int(bid)))

hands = sorted(hands, key=sortkey)
print(sum(rank * hand[1] for rank, hand in enumerate(hands, 1)))
