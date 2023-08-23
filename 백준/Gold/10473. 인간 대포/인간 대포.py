from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize

def get_dist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def get_walk(s, e):
    return get_dist(s[0], s[1], e[0], e[1]) / 5

def get_cannon(s, e):
    return abs(get_dist(s[0], s[1], e[0], e[1]) - 50) / 5 + 2

def push(s, e, w, c):
    matrix[s].append((w, e))
    matrix[s].append((c, e))

sx, sy = map(float, input().split())
ex, ey = map(float, input().split())
N = int(input())
points = [(sx, sy)] + [tuple(map(float, input().split())) for _ in range(N)] + [(ex, ey)]

matrix = [[] for _ in range(N + 1)]

for i in range(1, N + 2):
    matrix[0].append((get_walk((sx, sy), points[i]), i))
    for j in range(i + 1, N + 2):
        walk, cannon = get_walk(points[i], points[j]), get_cannon(points[i], points[j])
        push(i, j, walk, cannon)
        if j == N + 1:
            continue
        push(j, i, walk, cannon)


pq = []
heappush(pq, (0, 0))
visited = [INF] * (N + 2)
visited[0] = 0

while pq:
    cost, x = heappop(pq)
    if visited[x] < cost:
        continue
    if x == N + 1:
        print(cost)
        break
    for nc, nx in matrix[x]:
        temp = cost + nc
        if visited[nx] > temp:
            visited[nx] = temp
            heappush(pq, (temp, nx))