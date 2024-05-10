from collections import deque
import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
matrix = [list(input().strip()) for _ in range(N)]
nx, ny = map(int, input().split())
sx, sy = map(int, input().split())
cx, cy = map(int, input().split())

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def bfs(x, y):
    q = deque([(x, y)])
    visited = [[INF] * M for _ in range(N)]
    visited[x][y] = 0
    while q:
        cur_x, cur_y = q.popleft()
        for i in range(4):
            nxt_x, nxt_y = cur_x + dx[i], cur_y + dy[i]
            if 0 <= nxt_x < N and 0 <= nxt_y < M:
                if visited[nxt_x][nxt_y] == INF and matrix[nxt_x][nxt_y] == '0':
                    visited[nxt_x][nxt_y] = visited[cur_x][cur_y] + 1
                    q.append((nxt_x, nxt_y))
    return visited

nv = bfs(nx - 1, ny - 1)
sv = bfs(sx - 1, sy - 1)
cv = bfs(cx - 1, cy - 1)

result = INF
cnt = 0

for i in range(N):
    for j in range(M):
        a, b, c = nv[i][j], sv[i][j], cv[i][j]
        cur = max(a, b, c)
        if cur == INF:
            continue
        if cur < result:
            cnt = 1
            result = cur
        elif cur == result:
            cnt += 1

if result != INF:
    print(result)
    print(cnt)
else:
    print(-1)