"""
Day 10: Pipe Maze | Advent of Code 2023
"""

from enum import Enum
from math import ceil


class Moves(Enum):
    """Enum for moves"""
    RIGHT = (1, 0)
    LEFT = (-1, 0)
    UP = (0, -1)
    DOWN = (0, 1)


class Pipes(Enum):
    """Enum for pipe types"""
    START = "S"
    GROUND = "."
    HORIZONTAL = "-"
    VERTICAL = "|"
    TOP_LEFT = "J"
    TOP_RIGHT = "L"
    BOTTOM_LEFT = "7"
    BOTTOM_RIGHT = "F"

    @staticmethod
    def from_str(value: str) -> 'Pipes':
        """Return pipe type from string"""
        if value == ".":
            return Pipes.GROUND
        if value == "S":
            return Pipes.START
        if value == "-":
            return Pipes.HORIZONTAL
        if value == "|":
            return Pipes.VERTICAL
        if value == "J":
            return Pipes.TOP_LEFT
        if value == "L":
            return Pipes.TOP_RIGHT
        if value == "7":
            return Pipes.BOTTOM_LEFT
        if value == "F":
            return Pipes.BOTTOM_RIGHT
        return None

    @property
    def edges(self) -> list[Moves]:
        """Return list of possible exits"""
        if self == Pipes.GROUND:
            return []
        if self == Pipes.HORIZONTAL:
            return [Moves.LEFT, Moves.RIGHT]
        if self == Pipes.VERTICAL:
            return [Moves.UP, Moves.DOWN]
        if self == Pipes.TOP_LEFT:
            return [Moves.LEFT, Moves.UP]
        if self == Pipes.TOP_RIGHT:
            return [Moves.RIGHT, Moves.UP]
        if self == Pipes.BOTTOM_LEFT:
            return [Moves.LEFT, Moves.DOWN]
        if self == Pipes.BOTTOM_RIGHT:
            return [Moves.RIGHT, Moves.DOWN]
        return []

    def get_exit(self, entry: Moves) -> str:
        """Return the exit for the given entry"""
        if self == Pipes.GROUND:
            return None
        if self == Pipes.HORIZONTAL:
            if entry in self.edges:
                return entry
        if self == Pipes.VERTICAL:
            if entry in self.edges:
                return entry
        if self == Pipes.TOP_RIGHT:
            if entry == Moves.LEFT:
                return Moves.UP
            if entry == Moves.DOWN:
                return Moves.RIGHT
        if self == Pipes.TOP_LEFT:
            if entry == Moves.RIGHT:
                return Moves.UP
            if entry == Moves.DOWN:
                return Moves.LEFT
        if self == Pipes.BOTTOM_RIGHT:
            if entry == Moves.LEFT:
                return Moves.DOWN
            if entry == Moves.UP:
                return Moves.RIGHT
        if self == Pipes.BOTTOM_LEFT:
            if entry == Moves.RIGHT:
                return Moves.DOWN
            if entry == Moves.UP:
                return Moves.LEFT
        return None


def part_one(filename: str) -> int:
    """Solution for part one"""
    maze: list[list[str]] = []
    start: tuple[int, int] = (0, 0)
    with open(filename, encoding='utf-8') as f:
        for line in f.readlines():
            if not line.strip():
                continue

            if 'S' in line:
                start = (line.index('S'), len(maze))
            maze.append(list(line.strip()))

    init_moves = [Moves.UP, Moves.DOWN, Moves.LEFT, Moves.RIGHT]

    loop: list[str] = []
    current = start
    loop.append(maze[current[1]][current[0]])
    next_move = init_moves.pop(0)
    while True:
        current = (current[0] + next_move.value[0],
                   current[1] + next_move.value[1])
        current_pipe = Pipes.from_str(maze[current[1]][current[0]])
        if current_pipe is Pipes.START:
            break
        next_move = current_pipe.get_exit(next_move)
        if next_move is None:
            # reset
            loop = []
            current = start
            next_move = init_moves.pop(0)

        loop.append(maze[current[1]][current[0]])

    return ceil(len(loop)/2.)


def part_two(filename: str) -> int:
    """Solution for part two"""
    total = 0
    with open(filename, encoding='utf-8') as f:
        for line in f.readlines():
            if not line.strip():
                continue

    return total


if __name__ == "__main__":
    assert part_one("10.ex") == 8
    solution_part_one = part_one("10.in")
    print(f"{solution_part_one=}")

    assert part_two("10.ex") == 2
    solution_part_two = part_two("10.in")
    print(f"{solution_part_two=}")
