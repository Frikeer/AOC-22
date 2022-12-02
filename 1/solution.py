import os

with open(os.path.join('1','input.txt'), 'r') as f:
    input_data = f. read()

input_list = input_data.split("\n\n")
for i, e in enumerate(input_list):
    input_list[i] = e.split("\n")

max_calories = [0,0,0]

for i, e in enumerate(input_list):
    calories = 0
    for cal in e:
        calories += int(cal)
    if (calories > max_calories[0]):
        max_calories[2] = max_calories[1]
        max_calories[1] = max_calories[0]
        max_calories[0] = calories
    elif (calories > max_calories[1]):
        max_calories[2] = max_calories[1]
        max_calories[1] = calories
        
    elif (calories > max_calories[2]):
        max_calories[2] = calories

print(max_calories)
print(sum(max_calories))



