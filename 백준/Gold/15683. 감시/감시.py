import sys
input = sys.stdin.readline

N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]

cctvs = [
    (i, j, office[i][j])
    for i in range(N)
    for j in range(M)
    if 1 <= office[i][j] <= 5
]

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

options = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]],
}

ans = float('inf')

def dfs(idx, watched):
    global ans

    if idx == len(cctvs):
        cnt = 0
        for x in range(N):
            for y in range(M):
                if office[x][y] == 0 and not watched[x][y]:
                    cnt += 1
        ans = min(ans, cnt)
        return

    x, y, t = cctvs[idx]

    for od in options[t]:
        nw = [row[:] for row in watched]

        for d in od:
            nx, ny = x, y
            while True:
                nx += dirs[d][0]
                ny += dirs[d][1]
                if not (0 <= nx < N and 0 <= ny < M) or office[nx][ny] == 6:
                    break
                nw[nx][ny] = True

        dfs(idx + 1, nw)

watched = [[False] * M for _ in range(N)]
dfs(0, watched)

print(ans)