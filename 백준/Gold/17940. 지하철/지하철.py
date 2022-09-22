from heapq import heappop, heappush
import sys
INF = sys.maxsize
input = sys.stdin.readline
N, end = map(int, input().split())
temp = []
for i in range(N):
    q = int(input())
    temp.append(q)
matrix = [[] for _ in range(N)]
numbers = [list(map(int, input().rstrip().split())) for _ in range(N)]
for i in range(N):
    for j in range(i, N):
        if numbers[i][j] != 0:
            t = numbers[i][j]
            matrix[i].append((t, j, temp[j]))
            matrix[j].append((t, i, temp[i]))
start = []
heappush(start, [0, 0, 0, temp[0]])
visited = [INF] * N
visited[0] = 0
cnt = INF
while start:
    z, time, node, company = heappop(start)
    for k, v, com in matrix[node]:
        nx = time + k
        if visited[v] > nx:
            if v == end:
                if company != com:
                    if cnt >= z + 1:
                        visited[v] = nx
                        heappush(start, [z + 1, nx, v, com])
                        cnt = z + 1
                else:
                    if cnt >= z:
                        visited[v] = nx
                        heappush(start, [z, nx, v, com])
                        cnt = z
            else:
                if company != com:
                    visited[v] = nx
                    heappush(start, [z + 1, nx, v, com])
                else:
                    visited[v] = nx
                    heappush(start, [z, nx, v, com])
print(cnt, visited[end])