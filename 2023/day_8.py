"""
Day 8 | Advent of Code 2023
"""

from math import lcm


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


def find_ends(nodes: dict, starting_node: str, instructions: list) -> list[int]:
    """Find end of network"""
    i = 0
    current_node = starting_node
    end = False
    end_nodes = []
    steps = []
    while not end:
        for instruction in instructions:
            if instruction == "R":
                n = 1
            elif instruction == "L":
                n = 0

            current_node = nodes[current_node][n]
            i += 1
            if list(current_node)[-1] == 'Z':
                if current_node in end_nodes:
                    end = True
                    break
                end_nodes.append(current_node)
                steps.append(i)

    return steps


def part_two(filename: str) -> int:
    """Solution for part two"""
    instructions = []
    starting_nodes = []
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
            if list(node)[-1] == "A":
                starting_nodes.append(node)
            nodes[node] = (right[:-1], left[:-1])

    # print(starting_nodes)
    ends = {}
    for node in starting_nodes:
        ends[node] = find_ends(nodes, node, instructions)

    # print([end[-1] for end in ends.values()])
    return lcm(*[end[-1] for end in ends.values()])


if __name__ == "__main__":
    assert part_one("8a.ex") == 2
    assert part_one("8b.ex") == 6
    solution_part_one = part_one("8.in")
    print(f"{solution_part_one=}")

    assert part_two("8c.ex") == 6
    solution_part_two = part_two("8.in")
    print(f"{solution_part_two=}")
