from collections import deque
from heapq import heappush, heappop
import sys
input = sys.stdin.readline
N, M, cost = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
sx, sy = map(int, input().split())
dx, dy = [0,0,1,-1],[1,-1,0,0]
sx -= 1; sy -= 1
def bfs(sx, sy):
    start = deque()
    start.append((sx, sy))
    visited = [[-1] * N for _ in range(N)]
    visited[sx][sy] = 0
    while start:
        x, y = start.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if matrix[nx][ny] != 1 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    start.append((nx, ny))
    return visited
visited = bfs(sx, sy)
people = []
for i in range(M):
    msx, msy, mex, mey = map(int, input().split())
    msx -= 1; msy -= 1; mex -= 1; mey -= 1
    if visited[msx][msy] != -1:
        heappush(people, (visited[msx][msy], msx, msy, mex, mey))
if M == len(people):
    while people:
        c, msx, msy, mex, mey = heappop(people)
        cost -= c
        if cost < 0:
            print(-1)
            break
        visited = bfs(msx, msy)
        if visited[mex][mey] > cost or visited[mex][mey] == -1:
            print(-1)
            break
        else:
            cost -= visited[mex][mey]
            cost += (visited[mex][mey] * 2)
        visited = bfs(mex, mey)
        new_people = []
        for gar, rsx, rsy, rex, rey in people:
            heappush(new_people, (visited[rsx][rsy], rsx, rsy, rex, rey))
        people = new_people
    else:
        print(cost)
else:
    print(-1)