calories = []

with open("./1-input.txt") as f:
    cal = 0
    for line in f.readlines():
        if line == '\n':
            calories.append(cal)
            cal = 0
            continue
        cal += int(line)

first = max(calories)
print("[PART 1] Score:", first)
calories.remove(first)


second = max(calories)
# print(second)
calories.remove(second)

third = max(calories)
# print(third)
calories.remove(third)

print("[PART 2] Score:", first+second+third)