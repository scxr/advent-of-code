inp = open("./inp.txt").read().split("\n")
import string
def getScore(char):
    if char in string.ascii_uppercase:
        return ord(char) - 38
    else:
        return ord(char) - 96

def star1():
    ans = 0
    for i in inp:
        char = ''.join(set(i[:len(i)//2]).intersection(i[len(i)//2:]))
        ans += getScore(char)

    print(ans)

def star2():
    ans = 0
    chunks = []
    for i in range(0, len(inp), 3):
        chunks.append(inp[i:i + 3])
    for i in chunks:
        char = ''.join(set(''.join(set(i[0]).intersection(i[1]))).intersection(i[2]))
        ans += getScore(char)
    print(ans)
star2()
