import os, re

with open(os.path.join('3','input.txt'), 'r') as f:
    input_data = f.read()

input_data = input_data.split("\n")

grouped_input = [[input_data[r*3], input_data[r*3+1], input_data[r*3+2]] for r in range(len(input_data)//3)]

def identifier(lst):
   a = list(set(lst[0]) & set(lst[1]) & set(lst[2]))
   a = a[0]
   return a



alphabet = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# print(input_data[:9])
rucksack_sum = 0
for i in grouped_input:
    rucksack_sum += (alphabet.index(identifier(i)))
print(rucksack_sum)


