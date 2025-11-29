import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()

res = 0
l = 0

for r in range(N):
    limit = 0.9 * A[r]
    while A[l] < limit:
        l += 1
    res += r - l

print(res)