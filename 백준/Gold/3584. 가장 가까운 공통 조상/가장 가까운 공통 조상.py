import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    parent = [i for i in range(N + 1)]
    visited = [False] * (N + 1)
    for _ in range(N - 1):
        a, b = map(int, input().split())
        parent[b] = a
    s, e = map(int, input().split())
    visited[s] = True
    while s != parent[s]:
        s = parent[s]
        visited[s] = True
    while True:
        if visited[e]:
            print(e)
            break
        e = parent[e]