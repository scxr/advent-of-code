inp = open("./inp.txt").read().split("\n")

def star12():
    out = 0 #595
    out2 = 0 #952
    for line in inp:
        elf1, elf2 = line.strip().split(",")
        a, b = map(int, elf1.split("-"))
        c, d = map(int, elf2.split("-"))

        # part 1
        if a <= c <= b and a <= d <= b:
            out += 1
        elif c <= a <= d and c <= b <= d:
            out +=1

        # part 2
        if a <= c <= b or a <= d <= b:
            out2 += 1
        elif c <= a <= d or c <= b <= d:
            out2 +=1 
    print(out, out2)


star12()
