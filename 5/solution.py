import os
import re

with open(os.path.join('5', 'input.txt'), 'r') as f:
    input_data = f.read()
state, instructions = input_data.split("\n\n")

state_rows = state.split("\n")
index_row = state_rows[-1].replace(" ", "")
state_rows = state_rows[:-1]
instructions = instructions.split("\n")

for i, r in enumerate(state_rows):
    state_rows[i] = r.replace("   ", "[]").replace(" ", "")[1:-1].split("][")

REGEX = r"\d+"
regex = re.compile(REGEX)


def _parse_instructions(instruction):
    amount, from_column, to_column = regex.findall(instruction)
    return int(amount), int(from_column), int(to_column)


def _crate_finder(from_column, level=0):
    if state_rows[level][from_column-1] != "":
        value = state_rows[level][from_column-1]
        return value, level
    else:
        return _crate_finder(from_column=from_column, level=level+1)


def _target_finder(to_column, level=0, state_rows=state_rows):
    if state_rows[level][to_column-1] != "":
        state_rows = state_rows.insert(0, ['' for i in index_row])
        return 0, True
    if level == len(state_rows)-1:
        return level, False
    if (state_rows[level][to_column-1] == "" and state_rows[level+1][to_column-1] != ""):
        return level, False
    else:
        return _target_finder(to_column, level=level+1)


def move_crates_9000(instructions):
    amount, from_column, to_column = _parse_instructions(instructions)
    for i in range(int(amount)):
        from_value, from_level = _crate_finder(int(from_column))
        target_level, added_level = _target_finder(int(to_column))
        if added_level:
            state_rows[from_level+1][from_column-1] = ''
        else:
            state_rows[from_level][from_column-1] = ''
        state_rows[target_level][to_column-1] = from_value


def move_crates_9001(instructions, state_rows=state_rows):
    amount, from_column, to_column = _parse_instructions(instructions)
    moved_column = []
    for i in range(int(amount)):
        from_value, from_level = _crate_finder(int(from_column))
        target_level, added_level = _target_finder(int(to_column))
        if added_level:
            state_rows[from_level+1][from_column-1] = ''
        else:
            state_rows[from_level][from_column-1] = ''
        moved_column.append(from_value)
    for i in range(int(amount)):
        if state_rows[0][to_column-1] != '':
            state_rows.insert(0, ['' for i in index_row])
            state_rows[0][to_column-1] = moved_column[len(moved_column)-1-i]

        else:
            state_rows[target_level-i][to_column -
                                       1] = moved_column[len(moved_column)-1-i]


if False:
    for r in state_rows:
        print(r)
    print("_"*50)
    for i, r in enumerate(instructions):
        move_crates_9000(r)
    for r in state_rows:
        print(r)

if True:
    for r in state_rows:
        print(r)
    print("_"*50)
    for i, r in enumerate(instructions):
        # print(r)
        move_crates_9001(r)
    for r in state_rows:
        print(r)

"GCFGLDNJZ"
