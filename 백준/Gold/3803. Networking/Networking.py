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
    parents[y] = x

while True:
    line = input().strip()
    if line == '0':
        break
    N, M = map(int, line.split())
    edges = sorted([tuple(map(int, input().split())) for _ in range(M)], key=lambda x : x[2])
    parents = [i for i in range(N + 1)]
    answer = cnt = 0
    for a, b, c in edges:
        x, y = find(a), find(b)
        if x != y:
            union(x, y)
            cnt += 1
            answer += c
        if cnt == N - 1:
            break
    print(answer)
    input()