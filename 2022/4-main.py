
score = 0
with open("4-input.txt") as f:
    for line in f.readlines():
        if line.strip():
            first_section, second_section = line.strip().split(",")
            first_sections = set(range(int(first_section.split("-")[0]), int(first_section.split("-")[-1])+1))
            second_sections = set(range(int(second_section.split("-")[0]), int(second_section.split("-")[-1])+1))
            score += 1 if first_sections.issubset(second_sections) or second_sections.issubset(first_sections) else 0

print("[PART 1] Score:", score)


score = 0
with open("4-input.txt") as f:
    for line in f.readlines():
        if line.strip():
            first_section, second_section = line.strip().split(",")
            first_sections = set(range(int(first_section.split("-")[0]), int(first_section.split("-")[-1])+1))
            second_sections = set(range(int(second_section.split("-")[0]), int(second_section.split("-")[-1])+1))
            score += 1 if not first_sections.isdisjoint(second_sections) else 0

print("[PART 2] Score:", score)
