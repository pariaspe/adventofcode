"""
Day 9 | Advent of Code 2023
"""


def difference(iterable):
    """Return list of differences between adjacent elements"""
    return [y - x for x, y in zip(iterable, iterable[1:])]


def get_prediction(seq):
    """Return the prediction for the next value in the sequence"""
    partial = seq[-1]
    next_seq = difference(seq)
    while any(next_seq):
        partial += next_seq[-1]
        next_seq = difference(next_seq)
    return partial


def get_backward_prediction(seq):
    """Return the prediction for the previous value in the sequence"""
    firsts = [seq[0]]
    next_seq = difference(seq)
    while any(next_seq):
        firsts.insert(0, next_seq[0])
        next_seq = difference(next_seq)

    partial = 0
    while len(firsts) >= 1:
        n = firsts.pop(0)
        partial = n - partial
    return partial


def part_one(filename: str) -> int:
    """Solution for part one"""
    total = 0
    with open(filename, encoding='utf-8') as f:
        for line in f.readlines():
            if not line.strip():
                continue

            seq = [int(num) for num in line.strip().split()]
            total += get_prediction(seq)
    return total


def part_two(filename: str) -> int:
    """Solution for part two"""
    total = 0
    with open(filename, encoding='utf-8') as f:
        for line in f.readlines():
            if not line.strip():
                continue

            seq = [int(num) for num in line.strip().split()]
            total += get_backward_prediction(seq)
    return total


if __name__ == "__main__":
    assert part_one("9.ex") == 114
    solution_part_one = part_one("9.in")
    print(f"{solution_part_one=}")

    assert part_two("9.ex") == 2
    solution_part_two = part_two("9.in")
    print(f"{solution_part_two=}")
