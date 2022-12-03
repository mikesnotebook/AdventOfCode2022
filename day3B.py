from collections import Counter

score_values = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
score = 0

all_packs = open("day3_data.txt").read().split('\n')

for i in range(0,len(all_packs),3):
    group = all_packs[i:i+3]
    for item in group[0]:
        if item in group[1] and item in group[2]:
            score = score + score_values.find(item)
            break
print(score)

#And, as an unreadable list comprehension:
print(sum([score_values.find(list(Counter(all_packs[i]) & Counter(all_packs[i+1]) & Counter(all_packs[i+2]))[0]) for i in range(0,len(all_packs),3)]))
