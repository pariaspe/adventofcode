from itertools import compress

item_list = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

score = 0
with open("./3-input.txt") as f:
    for line in f.readlines():
        if not line.strip():
            break
        rucksack_items = list(line.strip())
        n = len(rucksack_items)//2
        first_compartment = set(rucksack_items[:n])
        second_compartment = set(rucksack_items[n:])
        
        bad_item = first_compartment.intersection(second_compartment)
        score += item_list.index(bad_item.pop()) + 1  # from 1 to 52

print("[PART 1] Score:", score)


score = 0
with open("./3-input.txt") as f:
    lines = f.readlines()
    lines_iter = iter(lines)
    for line in lines_iter:
       first_rucksack = set(line.strip())
       second_rucksack = set(next(lines_iter).strip())
       third_rucksack = set(next(lines_iter))

       common_item = first_rucksack.intersection(second_rucksack, third_rucksack)
       score += item_list.index(common_item.pop()) + 1  # from 1 to 52

print("[PART 2] Score:", score)