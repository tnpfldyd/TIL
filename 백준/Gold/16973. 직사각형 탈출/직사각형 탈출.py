import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

H, W, Sr, Sc, Fr, Fc = map(int, input().split())
Sr -= 1
Sc -= 1
Fr -= 1
Fc -= 1

ps = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(N):
    for j in range(M):
        ps[i + 1][j + 1] = ps[i][j + 1] + ps[i + 1][j] - ps[i][j] + board[i][j]

def can_move(r, c):
    r2 = r + H
    c2 = c + W
    return ps[r2][c2] - ps[r][c2] - ps[r2][c] + ps[r][c] == 0

visited = [[False] * M for _ in range(N)]
q = deque()
q.append((Sr, Sc, 0))
visited[Sr][Sc] = True

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

answer = -1

while q:
    r, c, d = q.popleft()
    if r == Fr and c == Fc:
        answer = d
        break

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]

        if nr < 0 or nc < 0 or nr + H > N or nc + W > M:
            continue
        if visited[nr][nc]:
            continue
        if not can_move(nr, nc):
            continue

        visited[nr][nc] = True
        q.append((nr, nc, d + 1))

print(answer)