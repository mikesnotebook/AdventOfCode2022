def init_lists(lines, instructions_line_number):
    lists = ['']
    line = lines[instructions_line_number-1]
    line = line.strip().replace(' ','')
    max_list_number = int(line[len(line)-1])
    for i in range(0,max_list_number):
        lists.append(list())

    for i in range(0,instructions_line_number - 1):
        init_crates(lists, len(lists), lines[i])

    reverse_crates(lists)
    return lists

def init_crates(lists, list_count, line):
    loc = 1
    for i in range(1, list_count):
        if len(line) >= loc and line[loc] != " ":
            lists[i].append(line[loc])
        loc = loc + 4             

def move_crates(instructions_line_number, lines, lists):
    for i in range(instructions_line_number + 1, len(lines)):
        line = lines[i]
        move_steps = line.split(' ')
        move_num = int(move_steps[1])
        source_num = int(move_steps[3])
        target_num = int(move_steps[5])
        for i in range(0,move_num):
            crate = lists[source_num].pop()
            lists[target_num].append(crate)
    return lists

def move_crates2(instructions_line_number, lines, lists):
    for i in range(instructions_line_number + 1, len(lines)):
        line = lines[i]
        move_steps = line.split(' ')
        move_num = int(move_steps[1])
        source_num = int(move_steps[3])
        target_num = int(move_steps[5])
        moving_crates = []
        for i in range(0,move_num):
            moving_crates.append(lists[source_num].pop())
        moving_crates.reverse()
        lists[target_num] = lists[target_num] + moving_crates
    return lists

def find_steps(lines):
    line_number = 0
    for i in range(0,len(lines)-1):
        if lines[i].strip() == "":
            line_number = i
            break
    return line_number

def reverse_crates(lists):
    for i in range(1,len(lists)):
        lists[i].reverse()
    
def get_answer(lists):
    answer = []
    for i in range(1,len(lists)):
        l = lists[i]
        answer.append(l[len(l)-1])
    return ''.join(answer)

#==============================================
lines = open("day5_data.txt").read().split('\n')

instructions_line_number = find_steps(lines)

#part 1
lists = init_lists(lines, instructions_line_number)
lists_part1 = move_crates(instructions_line_number, lines, lists)

#part 2
lists = init_lists(lines, instructions_line_number)
lists_part2 = move_crates2(instructions_line_number, lines, lists)


print(get_answer(lists_part1))
print(get_answer(lists_part2))

#part 1: QPJPLMNNR
#part 2: BQDNWJPVJ

    
