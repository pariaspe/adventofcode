from typing import List, AnyStr
from math import ceil
from collections import deque

with open("5-input.txt") as f:
    lines = f.readlines()

lines_stack = lines[:lines.index('\n')]
lines_moves = lines[lines.index('\n')+1:]

stacks = []
for line in lines_stack:
    if not stacks:
        stack_lenght = ceil(len(line)/4)
        stacks = [deque() for _ in range(stack_lenght)]

    crates = line.replace("    ", "_").replace(" ", "").replace("[", "").replace("]", "").strip()
    if crates.isdigit():
        break
    for i, crate in enumerate(crates):
        if crate != "_":
            stacks[i].append(crate)

for line in lines_moves:
    if not line.strip():
        break
    n, from_, to_ = line.strip().replace("move ", "").replace(" from ", ",").replace(" to ", ",").split(",")
    
    # PART ONE
    # for i in range(int(n)):
    #     moving_stack = stacks[int(from_)-1].popleft()
    #     stacks[int(to_)-1].appendleft(moving_stack)

    # PART TWO
    temp_stack = deque()
    for i in range(int(n)):
        temp_stack.appendleft(stacks[int(from_)-1].popleft())
    stacks[int(to_)-1].extendleft(temp_stack)


for stack in stacks:
    print(stack[0], end="")
print()