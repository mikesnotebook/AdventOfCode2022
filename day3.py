from collections import Counter

score_values = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
score = 0

all_packs = open("day3_data.txt").read().split('\n')

for pack in all_packs:
    compartment_size = int(len(pack)/2)
    compartment1 = pack[:compartment_size]
    compartment2 = pack[compartment_size:]
    common_item = list(Counter(compartment1) & Counter(compartment2))[0]
    score = score + score_values.find(common_item)
print(score)

#And, as an unreadable list comprehension:
print(sum([score_values.find(c) for c in [list(Counter(pack[:int(len(pack)/2)]) & Counter(pack[int(len(pack)/2):]).keys())[0] for pack in all_packs]]))


