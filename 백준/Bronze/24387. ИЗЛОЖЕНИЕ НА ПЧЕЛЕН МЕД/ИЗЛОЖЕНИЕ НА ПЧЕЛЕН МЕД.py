import sys
from itertools import permutations
input = sys.stdin.readline

A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for p in permutations(A):
    ans = max(ans, p[0]*B[0] + p[1]*B[1] + p[2]*B[2])

print(ans)