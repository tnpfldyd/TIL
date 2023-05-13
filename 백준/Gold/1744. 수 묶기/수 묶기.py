import sys
input = sys.stdin.readline
N = int(input())

pos = []
neg = []
zero = []
ans = []
for i in range(N):
    num = int(input())
    if num > 0:
        if num == 1:
            ans.append(num)
        else:
            pos.append(num)
    elif num < 0:
        neg.append(num)
    else:
        zero.append(num)

pos.sort()
neg.sort()

pSize = len(pos)
if pSize % 2 != 0:
    ans.append(pos[0])
for i in range(pSize - 1, 0, -2):
    big = pos[i]
    small = pos[i - 1]
    ans.append(big * small)

nSize = len(neg)
if nSize % 2 != 0:
    if len(zero) > 0:
        zero.pop()
    else:
        ans.append(neg[nSize - 1])
for i in range(0, nSize - 1, 2):
    small = neg[i]
    big = neg[i + 1]
    ans.append(small * big)

print(sum(ans))