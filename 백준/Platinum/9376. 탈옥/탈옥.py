from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
dx, dy = [0,0,1,-1], [1,-1,0,0]
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    matrix = [list('.' * (M+2))] + [list('.' + input().strip() + '.') for _ in range(N)] + [list('.' * (M+2))]
    start = []
    for i in range(N+2):
        for j in range(M+2):
            if matrix[i][j] == '$':
                start.append((i, j))
    def heap(a, b):
        start = []
        heappush(start, [0, a, b])
        visited = [[-1] * (M+2) for _ in range(N+2)]
        visited[a][b] = 0
        while start:
            cnt, x, y = heappop(start)
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N+2 and 0 <= ny < M+2:
                    if visited[nx][ny] == -1:
                        if matrix[nx][ny] == '#':
                            visited[nx][ny] = visited[x][y] + 1
                            heappush(start, [cnt + 1, nx, ny])
                        elif matrix[nx][ny] == '.' or matrix[nx][ny] == '$':
                            visited[nx][ny] = visited[x][y]
                            heappush(start, [cnt, nx, ny])
        return visited
    start1 = heap(start[0][0], start[0][1])
    start2 = heap(start[1][0], start[1][1])
    start3 = heap(0, 0)
    result = INF
    for i in range(N+2):
        for j in range(M+2):
            if start1[i][j] != -1 and start2[i][j] != -1 and start3[i][j] != -1:
                temp = start1[i][j]+start2[i][j]+start3[i][j]
                if matrix[i][j] == '*':
                    continue
                if matrix[i][j] == '#':
                    temp -= 2
                result = min(result, temp)
    print(result)