score_values = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
score = 0

all_packs = open("day3_data.txt").read().split('\n')

for pack in all_packs:
    pack_size = len(pack)
    compartment1 = pack[:int(pack_size/2)]
    compartment2 = pack[int(pack_size/2):]
    for item in compartment1:
        if item in compartment2:
            score = score + score_values.find(item)
            break
print(score)