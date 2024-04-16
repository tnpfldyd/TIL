import sys
input = sys.stdin.readline

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    if x < y:
        x, y = y, x
    parents[x] = y
T = int(input())
for _ in range(T):
    N = int(input())
    matrix = [list(map(int, (input().split()))) for _ in range(N)]
    parents = [i for i in range(N)]
    for i in range(N - 1):
        for j in range(i + 1, N):
            if not matrix[i][j]:
                continue
            x, y = find(i), find(j)
            if x != y:
                union(x, y)
    cnt = len(set(parents))
    print(N - cnt)