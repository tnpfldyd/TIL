from heapq import heappop, heappush
import sys
input = sys.stdin.readline
N = int(input())
matrix = [list(map(int,input().rstrip())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
start = []
heappush(start, [0, 0, 0])
visited[0][0] = 1
dx, dy = [0,0,1,-1], [1,-1,0,0]
while start:
    stone, x, y = heappop(start)
    if x == N-1 and y == N-1:
        print(stone)
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            if matrix[nx][ny] == 0:
                visited[nx][ny] = 1
                heappush(start, [stone+1, nx, ny])
            else:
                visited[nx][ny] = 1
                heappush(start, [stone, nx, ny])
