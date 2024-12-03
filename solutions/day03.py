import re

from utils.file_reader import read_input

memory = read_input(day=3)

# First part
# From the scrambled memory, only get the mul(144,241) as the regex displays
total = 0
for line in memory:
    mul_arr = re.findall("mul\(\d{1,3},\d{1,3}\)", line)
    for mul in mul_arr:
        x, y = re.sub('[^\d,]', '', mul).split(',')
        total += int(x) * int(y)

print(f"Total multipliction: {total}")

# Part two
# everything from part one, except do() and dont() are added
# Do the mul if do() else dont()
total_two = 0
action = True
for line in memory:
    mul_patt = "mul\(\d{1,3},\d{1,3}\)"
    action_patt = "(?:do\(\)|don't\(\))"
    pattern = f"(?:{mul_patt}|{action_patt})"

    for mul in re.findall(pattern, line):
        print(mul)
        # Check if it is a mul or not
        if "mul" in mul:
            x, y = re.sub('[^\d,]', '', mul).split(',')
            if action:
                total_two += int(x) * int(y)
        else:
            if "don't" in mul:
                action = False
            else:
                action = True

print(f"Total multipliction part two: {total_two}")