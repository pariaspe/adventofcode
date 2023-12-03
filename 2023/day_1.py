"""
Day 1 | Advent of Code 2023
"""


def part_one():
    """Solution for part one"""
    with open("1-input.txt", encoding='utf-8') as f:
        calibration_sum = 0
        for line in f.readlines():
            if not line.strip():
                break
            nums = list(map(lambda x: x if x.isdigit() else '', line))
            nums = "".join(nums)
            calibration_num = nums[0] + nums[-1]
            calibration_sum += int(calibration_num)

    return calibration_sum


numbers = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
           'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', }


def part_two(filename: str) -> int:
    """Solution for part two"""
    with open(filename, 'r', encoding='utf-8') as f:
        calibration_sum = 0
        for line in f.readlines():
            if not line.strip():
                break

            i = 0
            j = 0
            calibrations = []
            while i < len(line):
                for number, value in numbers.items():
                    if number in line[j:i]:
                        calibrations.append(value)
                        j = i - 1
                        break

                if line[i].isdigit():
                    calibrations.append(line[i])
                    j = i + 1

                i += 1

            nums = "".join(calibrations)
            # calibration_num = nums[0] if len(nums) == 1 else nums[0] + nums[-1]
            calibration_num = nums[0] + nums[-1]
            calibration_sum += int(calibration_num)
    return calibration_sum


if __name__ == "__main__":
    solution_part_one = part_one()
    print(f"{solution_part_one=}")

    assert part_two("1-test.txt") == 281
    assert part_two("1-test_2.txt") == 21
    solution_part_two = part_two("1-input.txt")
    print(f"{solution_part_two=}")
