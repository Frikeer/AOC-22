import os
import re

with open(os.path.join('5','test_input.txt'), 'r') as f:
    input_data = f.read()
state, instructions = input_data.split("\n\n")


state_rows = state.split("\n")
index_row = state_rows[-1]
state_rows = state_rows[:-1]

for i, r in enumerate(state_rows):
    state_rows[i] = r.replace("   ","[]").replace(" ","")[1:-1].split("][")
    # state_rows[i] = r[1:-1]

REGEX = r"\d+"
regex = re.compile(REGEX)


def parse_instructions(instruction):
    return regex.findall(instruction)
    



# print(state_rows)

print(parse_instructions("move 1 from 22 to 1"))