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

N, M = map(int, input().split())
edges = sorted([tuple(map(int, input().split())) for _ in range(M)], key=lambda x : -x[2])
parents = [i for i in range(N + 1)]
cnt = answer = 0

for a, b, c in edges:
    a, b = find(a), find(b)
    if a != b:
        union(a, b)
        cnt += 1
        answer += c
    if cnt == N - 1:
        print(answer)
        break
else:
    print(-1)