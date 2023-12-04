"""
Day 3 | Advent of Code 2023
"""


def check_around(grid: list[str], x: int, y: int) -> list[tuple[int, int]]:
    """Check around coordinates"""
    pose_numbers: list[tuple[int, int]] = []
    for i in range(x-1, x+2):
        if i < 0 or i >= len(grid):
            continue
        for j in range(y-1, y+2):
            if j < 0 or j >= len(grid[i]):
                continue

            if i == x and j == y:
                continue
            if grid[i][j].isdigit():
                pose_numbers.append((i, j))
    return pose_numbers


def get_number(row: str, y: int) -> int:
    """Get number from row"""
    num = ''
    i = y
    while row[i].isdigit():
        i -= 1
    i += 1
    while row[i].isdigit():
        num += row[i]
        i += 1
        if i >= len(row):
            i -= 1
            break
    return int(num), i


def part_one(filename: str) -> int:
    """Solution for part one"""
    grid: list[str] = []
    with open(filename, encoding='utf-8') as f:
        for line in f.readlines():
            if not line.strip():
                break
            grid.append(line.strip())

    engine_sum = 0
    num_poses = []
    for i, row in enumerate(grid):
        for j, element in enumerate(row):
            if not element.isalnum() and element != '.':
                print(element)
                num_poses += check_around(grid, i, j)

    engine_nums = {}
    for pose in num_poses:
        num, y = get_number(grid[pose[0]], pose[1])
        engine_nums[(pose[0], y)] = num

    for pose, value in engine_nums.items():
        engine_sum += value

    return engine_sum


def part_two(filename: str) -> int:
    """Solution for part two"""
    grid: list[str] = []
    with open(filename, encoding='utf-8') as f:
        for line in f.readlines():
            if not line.strip():
                break
            grid.append(line.strip())

    engine_sum = 0
    for i, row in enumerate(grid):
        for j, element in enumerate(row):
            if element == '*':
                engine_nums = {}
                for pose in check_around(grid, i, j):
                    num, y = get_number(grid[pose[0]], pose[1])
                    engine_nums[(pose[0], y)] = num

                if len(engine_nums.keys()) == 2:
                    engine_sum += list(engine_nums.values())[0] * \
                        list(engine_nums.values())[1]
    return engine_sum


if __name__ == "__main__":
    assert part_one("3-test.txt") == 4361
    solution_part_one = part_one("3-input.txt")
    print(f"{solution_part_one=}")

    assert part_two("3-test.txt") == 467835
    solution_part_two = part_two("3-input.txt")
    print(f"{solution_part_two=}")
