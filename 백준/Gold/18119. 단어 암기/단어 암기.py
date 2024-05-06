import sys
input = sys.stdin.readline
print = sys.stdout.write
t = lambda c : ord(c) - ord('a')
N, M = map(int, input().split())

words = []
for _ in range(N):
    word = input().strip()
    bit = 0
    for c in word:
        idx = t(c)
        bit |= (1 << idx)
    words.append(bit)

def solve():
    global words
    remem = 2 ** 26 - 1

    for _ in range(M):
        o,c = input().strip().split()
        idx = t(c)

        if o == '1':
            remem &= ~(1 << idx)
        else:
            remem |= 1 << idx

        cnt = 0
        for word in words:
            if remem & word == word:
                cnt += 1
        print('%d\n'%cnt)
solve()