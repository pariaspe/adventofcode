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

        print(f"{calibration_sum=}")


if __name__ == "__main__":
    part_one()
