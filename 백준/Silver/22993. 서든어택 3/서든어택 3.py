import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))
A1 = A[0]
others = sorted(A[1:])

cur = A1
for x in others:
    if cur > x:
        cur += x
    else:
        print("No")
        break
else:
    print("Yes")