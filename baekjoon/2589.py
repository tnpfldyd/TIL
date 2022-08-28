from collections import deque
N, M = map(int, input().split())
matrix = [list(input()) for _ in range(N)]
dx, dy = [0,0,1,-1],[1,-1,0,0]
temp = []
for x in range(N):
    for y in range(M):
        if matrix[x][y] == 'L':
            start = deque()
            start.append((x, y))
            visited = [[0] * M for _ in range(N)]
            visited[x][y] = 1
            while start:
                a, b = start.popleft()
                for i in range(4):
                    na, nb = a + dx[i], b + dy[i]
                    if 0 <= na < N and 0 <= nb < M:
                        if matrix[na][nb] == 'L' and visited[na][nb] == 0:
                            visited[na][nb] = visited[a][b] + 1
                            start.append((na, nb))
            temp.append(max(map(max, visited)))
print(max(temp) - 1)