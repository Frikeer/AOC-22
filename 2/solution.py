import os

with open(os.path.join('2','input.txt'), 'r') as f:
    input_data = f. read()

input_data = input_data.split("\n")

for i, e in enumerate(input_data):
    input_data[i] = e.split(" ")

scores = {'X':1, 'Y': 2, 'Z':3, 'L':0, 'D': 3, 'W':6}

def outcome(opponent, you):
    if opponent == 'A':
        if you == 'X':
            return (scores['X']+scores['D'])
        if you == 'Y':
            return (scores['Y']+scores['W'])
        if you == 'Z':
            return (scores['Z']+scores['L'])
    if opponent == 'B':
        if you == 'X':
            return (scores['X']+scores['L'])
        if you == 'Y':
            return (scores['Y']+scores['D'])
        if you == 'Z':
            return (scores['Z']+scores['W'])
    if opponent == 'C':
        if you == 'X':
            return (scores['X']+scores['W'])
        if you == 'Y':
            return (scores['Y']+scores['L'])
        if you == 'Z':
            return (scores['Z']+scores['D'])

def outcome_2(opponent, goal):
    if opponent == 'A':
        if goal == 'X':
            return (scores['Z']+scores['L'])
        if goal == 'Y':
            return (scores['X']+scores['D'])
        if goal == 'Z':
            return (scores['Y']+scores['W'])
    if opponent == 'B':
        if goal == 'X':
            return (scores['X']+scores['L'])
        if goal == 'Y':
            return (scores['Y']+scores['D'])
        if goal == 'Z':
            return (scores['Z']+scores['W'])
    if opponent == 'C':
        if goal == 'X':
            return (scores['Y']+scores['L'])
        if goal == 'Y':
            return (scores['Z']+scores['D'])
        if goal == 'Z':
            return (scores['X']+scores['W'])


total_score_a = 0

for e in input_data:
    # print(e)
    # print(outcome(e[0],e[1]))
    total_score_a += outcome(e[0],e[1])

total_score_b = 0

for e in input_data:
    # print(e)
    # print(outcome(e[0],e[1]))
    total_score_b += outcome_2(e[0],e[1])


print(total_score_a)
print(total_score_b)
