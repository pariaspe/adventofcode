"""
Day 4 | Advent of Code 2023
"""


def part_one(filename: str) -> int:
    """Solution for part one"""
    points = 0
    with open(filename, encoding='utf-8') as f:
        for line in f.readlines():
            if not line.strip():
                break

            _, card_numbers = line.split(':')
            winning_num, playing_num = card_numbers.split('|')
            winning_num = winning_num.strip().split(' ')
            playing_num = playing_num.strip().split(' ')

            i = 0
            for element in winning_num:
                if element.isdigit() and element in playing_num:
                    i += 1
            if i > 0:
                points += 2**(i-1)

    return points


def part_two(filename: str) -> int:
    """Solution for part two"""
    card_instances: dict[int, int] = {}
    with open(filename, encoding='utf-8') as f:
        for line in f.readlines():
            if not line.strip():
                break

            header, card_numbers = line.split(':')
            *_, card_num = header.strip().split(' ')
            if int(card_num) not in card_instances:
                card_instances[int(card_num)] = 1
            else:
                card_instances[int(card_num)] += 1
            winning_num, playing_num = card_numbers.split('|')
            winning_num = winning_num.strip().split(' ')
            playing_num = playing_num.strip().split(' ')

            i = 0
            for element in winning_num:
                if element.isdigit() and element in playing_num:
                    i += 1

            n_copies = card_instances[int(card_num)]
            for j in range(i+1):
                if j == 0:
                    continue
                if int(card_num)+j in card_instances:
                    card_instances[int(card_num)+j] += 1 * n_copies
                else:
                    card_instances[int(card_num)+j] = 1 * n_copies

    return sum(list(card_instances.values()))


if __name__ == "__main__":
    assert part_one("4-test.txt") == 13
    solution_part_one = part_one("4-input.txt")
    print(f"{solution_part_one=}")

    assert part_two("4-test.txt") == 30
    solution_part_two = part_two("4-input.txt")
    print(f"{solution_part_two=}")
