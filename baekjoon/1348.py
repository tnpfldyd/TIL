from collections import deque
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
matrix = []
place, car = [], []
dx, dy = [0,0,1,-1],[1,-1,0,0]
for i in range(N):
    arr = list(input().strip())
    for j in range(M):
        if arr[j] == 'P':
            place.append((i, j))
        elif arr[j] == 'C':
            car.append((i, j))
    matrix.append(arr)

def bfs(x, y, cur):
    start = deque()
    start.append((x, y))
    visited = [[-1] * M for _ in range(N)]
    visited[x][y] = 0
    while start:
        x, y = start.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == -1 and matrix[nx][ny] != 'X':
                    visited[nx][ny] = visited[x][y] + 1
                    start.append((nx, ny))
    for i, h in enumerate(place):
        x, y = h
        if visited[x][y] == -1:
            dist[cur][i] = INF
        else:
            graph[cur].append(i)
            dist[cur][i] = visited[x][y]

def dfs(cur, time):
    for i in graph[cur]:
        if visited[i] or dist[cur][i] > time:
            continue
        visited[i] = True
        if parent[i] == -1 or dfs(parent[i], time):
            parent[i] = cur
            return True
    return False

if len(car) > len(place):
    print(-1)
else:
    dist = [[-1] * len(place) for _ in range(len(car))]
    graph = [[] for _ in range(len(car))]
    for i, h in enumerate(car):
        x, y = h
        bfs(x, y, i)
    answer, l, r = -1, 0, (N + 1) * (M + 1)
    while l <= r:
        mid = (l + r) // 2
        cnt = 0
        parent = [-1] * (len(place) + 1)
        for i in range(len(car)):
            visited = [False] * (len(place) + 1)
            if dfs(i, mid):
                cnt += 1
        if cnt == len(car):
            answer = mid
            r = mid - 1
        else:
            l = mid + 1
    print(answer)

