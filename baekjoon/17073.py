from collections import defaultdict
import sys
input = sys.stdin.readline

N, W = list(map(int, input().split()))
matrix = defaultdict(list)
for _ in range(N - 1):
    u, v = map(int, input().split())
    matrix[u].append(v)
    matrix[v].append(u)

del matrix[1]

count = 0
for childs in matrix.values():
    if len(childs) == 1:
        count += 1

print(round(W / count, 10))