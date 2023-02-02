from heapq import heappop, heappush
import sys
INF = sys.maxsize
input = sys.stdin.readline
number = 1
while True:
    N = int(input())
    if not N:
        break
    matrix = [list(map(int, input().strip().split())) for _ in range(N)]
    visited = [[INF] * N for _ in range(N)]
    visited[0][0] = matrix[0][0]

    start = []
    heappush(start, (matrix[0][0], 0, 0))
    dx, dy = [0,0,1,-1], [1,-1,0,0]
    while start:
        cnt, x, y = heappop(start)
        if (x, y) == (N-1, N-1):
            print(f'Problem {number}: {cnt}')
            break
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                next_cost = cnt + matrix[nx][ny]
                if visited[nx][ny] > next_cost:
                    visited[nx][ny] = next_cost
                    heappush(start, (next_cost, nx, ny))
    number += 1