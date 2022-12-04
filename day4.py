def is_complete_overlap(a1,b1,a2,b2):
    overlaps = 0
    if a1 <= a2 and b1 >= b2:
        overlaps = 1
    elif a2 <= a1 and b2 >= b1:
        overlaps = 1
    return overlaps

def is_partial_overlap(a1,b1,a2,b2):
    overlaps = 0
    if a1 >= a2 and a1 <= b2:
        overlaps = 1
    elif b1 >= a2 and b1 <= b2:
        overlaps = 1
    elif a2 >= a1 and a2 <= b1:
        overlaps = 1
    elif b2 >= a1 and b2 <= b1:
        overlaps = 1
    return overlaps

assignments = open("day4_data.txt").read().split('\n')
overlap_count = 0
partial_overlap_count = 0
for assignment in assignments:
    elf1_start,elf1_end,elf2_start,elf2_end  = map(int,assignment.replace(",","-").split("-"))
    overlap_count = overlap_count + is_complete_overlap(elf1_start, elf1_end, elf2_start, elf2_end)
    partial_overlap_count = partial_overlap_count + is_partial_overlap(elf1_start, elf1_end, elf2_start, elf2_end)
print(overlap_count)
print(partial_overlap_count)

#And, as an difficult to read list comprehension
print("complete overlap: {}".format(sum([is_complete_overlap(int(a[0]),int(a[1]),int(a[2]),int(a[3])) for a in [assignment.replace(",","-").split("-") for assignment in assignments]])))
print("partial overlap: {}".format(sum([is_partial_overlap(int(a[0]),int(a[1]),int(a[2]),int(a[3])) for a in [assignment.replace(",","-").split("-") for assignment in assignments]])))