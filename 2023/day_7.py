"""
Day 7 | Advent of Code 2023
"""

from enum import Enum
from collections import Counter, UserDict


class Card(Enum):
    """Card values"""
    A = 14
    K = 13
    Q = 12
    J = 11
    T = 10


class Hand(UserDict):
    """A hand of cards"""

    def __init__(self, hand: str, bid: int) -> None:
        """Initialize a hand of cards"""
        super().__init__()
        self.hand = hand
        self.data = Counter(hand)
        self.bid = int(bid)

    @property
    def ranking(self) -> int:
        """Return the ranking of the hand

        Five of a kind: 7
        Four of a kind: 6
        Full house: 5
        Three of a kind: 4
        Two pair: 3
        One pair: 2
        High card: 1
        """
        hand = self.data.values()
        if 5 in hand:
            return 7
        if 4 in hand:
            return 6
        if 3 in hand and 2 in hand:
            return 5
        if 3 in hand:
            return 4
        if 2 in hand and len(hand) == 3:
            return 3
        if 2 in hand:
            return 2
        return 1

    @property
    def stregth(self) -> int:
        """Return the strength of the hand"""
        strengh = ""
        for card in self.hand:
            if card.isdigit():
                strengh += "0" + card
            else:
                strengh += str(Card[card].value)
        return int(strengh)

    def __repr__(self) -> str:
        """Return the hand"""
        return self.hand

    def __eq__(self, __other: 'Hand') -> bool:
        return self.data == __other.data

    def __lt__(self, __other: 'Hand') -> bool:
        if self.ranking == __other.ranking:
            return self.stregth < __other.stregth
        return self.ranking < __other.ranking


def part_one(filename: str) -> int:
    """Solution for part one"""
    hands: list[Hand] = []
    with open(filename, encoding='utf-8') as f:
        for line in f.readlines():
            if not line.strip():
                break

            hand, bid = line.strip().split(" ")
            hands.append(Hand(hand, bid))

    sorted_hands = sorted(hands)
    winnings = 0
    for i, hand in enumerate(sorted_hands):
        winnings += hand.bid * (i + 1)
    return winnings


def part_two(filename: str) -> int:
    """Solution for part two"""
    with open(filename, encoding='utf-8') as f:
        for line in f.readlines():
            if not line.strip():
                break

    return 0


if __name__ == "__main__":
    assert part_one("7.ex") == 6440
    solution_part_one = part_one("7.in")
    print(f"{solution_part_one=}")

    assert part_two("7.ex") == 5905
    solution_part_two = part_two("7.in")
    print(f"{solution_part_two=}")
