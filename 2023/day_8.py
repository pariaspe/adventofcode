"""
Day 8 | Advent of Code 2023
"""


def part_one(filename: str) -> int:
    """Solution for part one"""
    instructions = []
    nodes = {}
    with open(filename, encoding='utf-8') as f:
        for line in f.readlines():
            if not line.strip():
                continue

            if not instructions:
                instructions = list(line.strip())
                continue

            node, paths = line.strip().split(" = (")
            right, left = paths.split(" ")
            nodes[node] = (right[:-1], left[:-1])

    i = 0
    current_node = "AAA"
    end = False
    while not end:
        for instruction in instructions:
            if instruction == "R":
                n = 1
            elif instruction == "L":
                n = 0

            current_node = nodes[current_node][n]
            i += 1
            if current_node == 'ZZZ':
                end = True
                break

    return i


def part_two(filename: str) -> int:
    """Solution for part two"""
    with open(filename, encoding='utf-8') as f:
        for line in f.readlines():
            if not line.strip():
                break

    return 0


if __name__ == "__main__":
    assert part_one("8a.ex") == 2
    assert part_one("8b.ex") == 6
    solution_part_one = part_one("8.in")
    print(f"{solution_part_one=}")

    assert part_two("8a.ex") == 71503
    solution_part_two = part_two("8.in")
    print(f"{solution_part_two=}")
