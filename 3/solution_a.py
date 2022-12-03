import os

with open(os.path.join('3','input.txt'), 'r') as f:
    input_data = f.read()

alphabet = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

input_data = input_data.split("\n")
pack_list = [[s[:len(s)//2], s[len(s)//2:]] for s in input_data]

def identifier(lst):
   a = list(set(lst[0]) & set(lst[1]))
   a = a[0]
   return a

# print(input_data[0])

# print(pack_list[0])
rucksack_sum = 0
for i in pack_list:
    rucksack_sum += (alphabet.index(identifier(i)))
    # print(identifier(i))
print(rucksack_sum)
