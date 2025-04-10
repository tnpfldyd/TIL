import sys
import bisect

input = sys.stdin.readline

N, M = map(int, input().split())
A = [int(input()) for _ in range(N)]
D_list = [int(input()) for _ in range(M)]

B = sorted(A)

for D in D_list:
    index = bisect.bisect_left(B, D)
    if index < N and B[index] == D:
        print(index)
    else:
        print(-1)