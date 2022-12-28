from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M, K = map(int, input().split())
matrix = [[] for _ in range(N)]
max_cost = 0
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((t, b))
    matrix[b].append((t, a))
    if max_cost < t:
        max_cost = t
def dijkstra(s, limit):
    start = []
    heappush(start, (0 , s))
    visited = [INF] * N
    visited[s] = 0
    while start:
        cost, node = heappop(start)
        if cost > visited[node]:
            continue
        for k, v in matrix[node]:
            temp = cost
            if k > limit:
                temp += 1
            if visited[v] > temp:
                visited[v] = temp
                heappush(start, (temp, v))
    return True if visited[N-1] <= K else False
left, right = 0, max_cost
result = -1
while left <= right:
    mid = (left + right) // 2
    if dijkstra(0, mid):
        right = mid - 1
        result = mid
    else:
        left = mid + 1
print(result)
