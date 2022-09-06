from heapq import heappop, heappush
import sys
input = sys.stdin.readline
cnt = 1
while True:
    N = int(input())
    if N == 0:
        break
    matrix = [list(map(int,input().rstrip().split())) for _ in range(N)]
    visited = [[9999999]*N for _ in range(N)]
    start = []
    heappush(start, [matrix[0][0], 0, 0])
    visited[0][0] = matrix[0][0]
    dx, dy = [0,0,1,-1], [1,-1,0,0]
    while start:
        stone, x, y = heappop(start)
        if x == N-1 and y == N-1:
            print(f'Problem {cnt}: {visited[x][y]}')
            break
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                new_stone = stone + matrix[nx][ny]
                if new_stone < visited[nx][ny]:
                    visited[nx][ny] = new_stone
                    heappush(start, [new_stone, nx, ny])
    cnt += 1