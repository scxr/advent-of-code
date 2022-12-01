inp = open("input.txt").read().split("\n")
def star1():
    curr = 0
    answer = 0

    for i in inp:
        
        if i == "":
            if curr > answer:
                answer = curr
            curr = 0
        else:
            curr += int(i)
    print(answer)
def star2():
    answer = []
    curr = 0
    for i in inp:
        if i == "":
            answer.append(curr)
            curr = 0
        else:
            curr += int(i)
    print(sum(sorted(answer)[::-1][0:3]))
star2()
