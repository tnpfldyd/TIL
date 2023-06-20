from heapq import heappop, heappush
import sys
input = sys.stdin.readline

while True:
    N, M = map(int, input().split())
    if not N and not M:
        break
    matrix = [[] for _ in range(N)]
    total = 0
    for _ in range(M):
        a, b, t = map(int, input().split())
        matrix[a].append((t, b))
        matrix[b].append((t, a))
        total += t
    visited = [False] * N
    visited[0] = True
    pq = []
    result = 0
    for i in range(len(matrix[0])):
        heappush(pq, (matrix[0][i]))
    while pq:
        cost, cur = heappop(pq)
        if not visited[cur]:
            visited[cur] = True
            result += cost
            for nc, nn in matrix[cur]:
                if not visited[nn]:
                    heappush(pq, (nc, nn))
    print(total - result)