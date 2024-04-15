import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
N, Q = map(int, input().split())
edges = sorted([tuple(map(int, input().split())) for _ in range(Q)], key=lambda x : (x[2], x[3]))
parents = [i for i in range(N + 1)]

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    if x < y:
        x, y = y, x
    parents[x] = y
cnt = result = time = 0    
for a, b, c, t in edges:
    x, y = find(a), find(b)
    if x != y:
        union(x, y)
        cnt += 1
        result += c
        time = max(time, t)
    if cnt == N - 1:
        print(time, result)
        break
else:
    print(-1)