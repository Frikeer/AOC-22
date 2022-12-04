import os

with open(os.path.join('4','input.txt'), 'r') as f:
    input_data = f.read()
input_data = input_data.split("\n")

for i, e in enumerate(input_data):
    input_data[i] = e.split(",")


def span_to_list(span):
    span_edges = span.split("-")
    span_list = []
    for n in range(int(span_edges[0]),int(span_edges[1])+1):
        span_list.append(n)
    return span_list

def check_overlap(span_pair):
    span_0 = span_to_list(span_pair[0])
    span_1 = span_to_list(span_pair[1])

    overlap_list = list(set(span_0) & set(span_1))
    if len(overlap_list) == 0:
        return False
    else: 
        return True

def check_full_overlap(span_pair):
    span_0 = span_to_list(span_pair[0])
    span_1 = span_to_list(span_pair[1])

    overlap_list = list(set(span_0) & set(span_1))
    full_overlap = (len(overlap_list) == len(span_0) or len(overlap_list) == len(span_1))

    return overlap_list, full_overlap


nbr_full_overlaps = 0
for p in input_data:
    _, full_overlap = check_full_overlap(p)
    if full_overlap:
        nbr_full_overlaps += 1

print("Nbr of full overlaps (task a): " + str(nbr_full_overlaps))

nbr_of_overlaps = 0
for p in input_data:
    overlap = check_overlap(p)
    if overlap:
        nbr_of_overlaps += 1


print("Nbr of overlaps (task b): " + str(nbr_of_overlaps))


