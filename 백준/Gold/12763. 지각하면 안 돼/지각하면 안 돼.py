from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N = int(input())
time, money = map(int, input().split())
M = int(input())
matrix = [[] for _ in range(N)]
for _ in range(M):
    a, b, t, m = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((m, t, b))
    matrix[b].append((m, t, a))
time_visit = [INF] * N
money_visit = [INF] * N
time_visit[0] = 0
money_visit[0] = 0
start = []
heappush(start, (0, 0, 0))
while start:
    mon, x, node = heappop(start) # 
    for k, y, v in matrix[node]:
        nx, ny = mon+k, x+y
        if nx <= money and ny <= time:
            if money_visit[v] > nx:
                money_visit[v] = nx
                heappush(start, (nx, ny, v))
            if time_visit[v] > ny:
                time_visit[v] = ny
                heappush(start, (nx, ny, v))
print(money_visit[N-1] if money_visit[N-1] != INF else -1)