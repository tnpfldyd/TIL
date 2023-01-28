from collections import deque
import sys, copy, itertools
input = sys.stdin.readline

N, M, G, R = map(int, input().split())
matrix = [list(map(int, input().strip().split())) for _ in range(N)]
land = []
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 2:
            land.append((i, j))
dx, dy = [0,0,1,-1], [1,-1,0,0]
def bfs(map, arr, green):
    cnt = 0
    r_q, g_q = deque(), deque()
    for x, y in arr:
        if (x, y) in green:
            g_q.append((x, y))
            map[x][y] = 3
        else:
            r_q.append((x, y))
            map[x][y] = 4
    while g_q:
        g_temp, r_temp = set(), set()
        while g_q:
            x, y = g_q.popleft()
            map[x][y] = 3
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < M:
                    if map[nx][ny] == 1 or map[nx][ny] == 2:
                        g_temp.add((nx, ny))
        while r_q:
            x, y = r_q.popleft()
            map[x][y] = 4
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < M:
                    if map[nx][ny] == 1 or map[nx][ny] == 2:
                        r_temp.add((nx, ny))
        inter = g_temp & r_temp
        g_temp -= inter; r_temp -= inter
        for x, y in inter:
            map[x][y] = 5
            cnt += 1
        for x, y in g_temp:
            map[x][y] = 3
        for x, y in r_temp:
            map[x][y] = 4
        g_q.extend(g_temp); r_q.extend(r_temp)
    return cnt

answer = 0
for i in itertools.combinations(land, G + R):
    for j in itertools.combinations(i, G):
        copy_matrix = copy.deepcopy(matrix)
        ret = bfs(copy_matrix, i, j)
        if answer < ret:
            answer = ret
print(answer)