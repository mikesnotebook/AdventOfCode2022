all_snacks = open("a1_data.txt").read()
sums = [sum([int(snack) for snack in snack_sack.split('\n')]) for snack_sack in all_snacks.split('\n\n')]
sums.sort(reverse=True)
print(sum(sums[:3]))


