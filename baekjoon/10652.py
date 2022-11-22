from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
B, E, P, N, M = map(int, input().split())
matrix = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append(b)
    matrix[b].append(a)

def heap(name, s):
    visited = [INF] * N
    visited[s] = 0
    start = []
    heappush(start, [0, s])
    while start:
        x, node = heappop(start)
        if x > visited[node]:
            continue
        for next in matrix[node]:
            nx = x + name
            if visited[next] > nx:
                visited[next] = nx
                heappush(start, [nx, next])
    return visited
Bessie = heap(B, 0)
Elsie = heap(E, 1)
Fianl = heap(P, N-1)
answer = INF
for i in range(N):
    temp = Bessie[i] + Elsie[i] + Fianl[i]
    if answer > temp:
        answer = temp
print(answer)