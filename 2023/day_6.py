"""
Day 4 | Advent of Code 2023

T = Tcharge + Trace

speed = Tcharge * 1
dist = speed * Trace
dist = Tcharge * Trace
dist = Tcharge * (T - Tcharge)
dist = Tcharge * T - Tcharge^2
Tcharge = T/2 +- sqrt(T^2 - 4*dist)/2

"""

from math import sqrt, ceil, floor


def get_t_charge(dist: float, time: float) -> tuple[float]:
    """Get time to charge"""
    x1 = time/2.0 + sqrt(time**2.0 - 4.0*dist)/2.0
    x2 = time/2.0 - sqrt(time**2.0 - 4.0*dist)/2.0

    return (x1, x2)


def part_one(filename: str) -> int:
    """Solution for part one"""
    with open(filename, encoding='utf-8') as f:
        for line in f.readlines():
            if not line.strip():
                break

            if line.startswith('Time'):
                _, time = line.strip().split(':')
                time = [float(x) for x in time.strip().split()]
                continue

            if line.startswith('Distance'):
                _, distance = line.strip().split(':')
                distance = [float(x) for x in distance.strip().split()]
                continue

    result = 1
    for d, t in zip(distance, time):
        x1, x2 = get_t_charge(d, t)
        lower = floor(x1) if x1 < x2 else floor(x2)
        upper = ceil(x2) if x1 < x2 else ceil(x1)
        result *= (upper - lower - 1)

    return result


def part_two(filename: str) -> int:
    """Solution for part two"""
    with open(filename, encoding='utf-8') as f:
        for line in f.readlines():
            if not line.strip():
                break

    return 0


if __name__ == "__main__":
    assert part_one("6.ex") == 288
    solution_part_one = part_one("6.in")
    print(f"{solution_part_one=}")

    # assert part_two("4-test.txt") == 30
    # solution_part_two = part_two("4-input.txt")
    # print(f"{solution_part_two=}")
