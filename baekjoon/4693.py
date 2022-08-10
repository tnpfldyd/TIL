import sys
input = sys.stdin.readline
while True:
    w, h = map(int, input().rstrip().split())
    if w == 0 and h == 0:
        break
    matrix = [list(map(int, input().rstrip().split())) for _ in range(h)]
    dx, dy = [-1, 0, 1, 0, 1, -1, 1, -1], [0, -1, 0, 1, 1, 1, -1, -1]
    visited = [[False] * w for _ in range(h)]
    cnt = 0
    for x in range(h):
        for y in range(w):
            if matrix[x][y] == 1 and visited[x][y] == False:
                cnt += 1
                visited[x][y] = True
                start = [(x, y)]
                while start:
                    a, b = start.pop()
                    for k in range(8):
                        nx = a + dx[k]
                        ny = b + dy[k]
                        if 0 <= nx < h and 0 <= ny < w:
                            if matrix[nx][ny] == 1 and visited[nx][ny] == False:
                                visited[nx][ny] = True
                                start.append((nx, ny))
    print(cnt)