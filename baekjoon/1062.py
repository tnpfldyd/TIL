import sys
input = sys.stdin.readline

checked = 0
word = []
N, K = map(int, input().split())

maxi = 0

def DFS(toPick, start, checked):
    global maxi
    
    if toPick == 0:
        cnt = 0
        for w in word:
            if w & checked == w:
                cnt += 1
        if maxi < cnt:
            maxi = cnt
        return
    
    for i in range(start, 26):
        if checked & (1 << i) == 0:
            checked |= (1 << i)
            DFS(toPick - 1, i, checked)
            checked &= ~(1 << i)

for _ in range(N):
    w = input().strip()
    num = 0
    for c in w:
        num |= 1 << (ord(c) - ord('a'))
    word.append(num)

if K < 5:
    print(0)
elif K == 26:
    print(N)
else:
    checked |= 1 << (ord('a') - ord('a'))
    checked |= 1 << (ord('n') - ord('a'))
    checked |= 1 << (ord('t') - ord('a'))
    checked |= 1 << (ord('i') - ord('a'))
    checked |= 1 << (ord('c') - ord('a'))
    DFS(K - 5, 0, checked)
    print(maxi)