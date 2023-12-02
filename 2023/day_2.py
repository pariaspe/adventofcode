"""
Day 2 | Advent of Code 2023
"""

from dataclasses import dataclass


@dataclass
class Game:
    """Game class"""
    index: int
    red: int = 0
    green: int = 0
    blue: int = 0

    @classmethod
    def from_string(cls, string: str):
        """Create Game object from string"""
        header, body = string.split(':')
        _, index = header.split(' ')
        red, green, blue = 0, 0, 0
        for throw in body.split(';'):
            for subset in throw.split(','):
                value, color = subset.strip().split(' ')
                if color == 'red' and int(value) > red:
                    red = int(value)
                elif color == 'green' and int(value) > green:
                    green = int(value)
                elif color == 'blue' and int(value) > blue:
                    blue = int(value)
        return cls(int(index), int(red), int(green), int(blue))

    def is_valid(self, r: int, g: int, b: int) -> bool:
        """Check if game is valid"""
        return self.red <= r and self.green <= g and self.blue <= b

    def power_sum(self) -> int:
        """Return power sum of values"""
        return self.red * self.green * self.blue


def part_one(filename: str, key_input: tuple[int, int, int]) -> int:
    """Solution for part one"""
    games: list[Game] = []
    with open(filename, encoding='utf-8') as f:
        for line in f.readlines():
            if not line.strip():
                break
            new_game = Game.from_string(line)
            if new_game.is_valid(*key_input):
                games.append(new_game)
    return sum(game.index for game in games)


def part_two(filename: str) -> int:
    """Solution for part two"""
    games: list[Game] = []
    with open(filename, encoding='utf-8') as f:
        for line in f.readlines():
            if not line.strip():
                break
            new_game = Game.from_string(line)
            games.append(new_game)
    return sum(game.power_sum() for game in games)


if __name__ == "__main__":
    assert part_one("2-input_test.txt", (12, 13, 14)) == 8
    solution_part_one = part_one("2-input.txt", (12, 13, 14))
    print(f"{solution_part_one=}")

    assert part_two("2-input_test.txt") == 2286
    solution_part_two = part_two("2-input.txt")
    print(f"{solution_part_two=}")
