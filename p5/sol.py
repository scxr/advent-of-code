with open("inp.txt", "r") as f:
    input_str = f.read().splitlines()
def star12(input_str, pt2):
    crates = [['N', 'S', 'D', 'C', 'V', 'Q', 'T'], ['M', 'F', 'V'], ['F', 'Q', 'W', 'D', 'P', 'N', 'H', 'M'], ['D', 'Q', 'R', 'T', 'F'], ['R', 'F', 'M', 'N', 'Q', 'H', 'V', 'B'], ['C', 'F', 'G', 'N', 'P', 'W', 'Q'], ['W', 'F', 'R', 'L', 'C', 'T'], ['T', 'Z', 'N', 'S'], ['M', 'S', 'D', 'J', 'R', 'Q', 'H', 'N']]
    for line in input_str[10:]:
        todo = line.split(" ")
        num, frm, to = int(todo[1]), int(todo[3]) -1, int(todo[5]) -1
        if not pt2:
            for i in range(num):
                crates[to].append(crates[frm].pop())
        else:
            tomove = crates[frm][-num:]
            crates[frm] = crates[frm][:-num]
            crates[to] = crates[to] + tomove
    
    return "".join(crates[i][-1] for i in range(9))



# Part 1: FRDSQRRCD
# Part 2: HRFTQVWNN
print ("Part 1:", star12(input_str, False))
print ("Part 2:", star12(input_str, True))