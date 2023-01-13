from heapq import heappop, heappush
import sys
INF = sys.maxsize
input = sys.stdin.readline
N = int(input())
N += 1
matrix = [[1] * N for _ in range(N)]
sx, sy, ex, ey = map(int, input().split())
K, M = int(input()), int(input())
for _ in range(M):
    load = list(map(int, input().strip().split()))
    i = load[0]
    cnt = 1
    for j in range(i-1):
        si, sj, ei, ej = min(load[cnt], load[cnt+2]), min(load[cnt+1], load[cnt+3]), max(load[cnt], load[cnt+2]), max(load[cnt+1], load[cnt+3])
        for x in range(si, ei+1):
            for y in range(sj, ej+1):
                matrix[x][y] = K
        cnt += 2
visited = [[INF] * N for _ in range(N)]
dx, dy = [0,0,1,-1], [1,-1,0,0]
start = []
heappush(start, (matrix[sx][sy], sx, sy, 4, []))
visited[sx][sy] = matrix[sx][sy]
result = []
while start:
    cost, x, y, dir, load = heappop(start)
    if cost > visited[x][y]:
        continue
    if (x, y) == (ex, ey):
        print(cost)
        result = load
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            next_cost = cost + matrix[nx][ny]
            if visited[nx][ny] > next_cost:
                visited[nx][ny] = next_cost
                if i != dir:
                    heappush(start, (next_cost, nx, ny, i, load + [(x, y)]))
                else:
                    heappush(start, (next_cost, nx, ny, i, load))
result.append((ex, ey))
print(len(result), end = ' ')
for x, y in result:
    print(x, y, end= ' ')