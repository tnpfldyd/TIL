import sys
input = sys.stdin.readline
result = [list(map(int, input().split())) for _ in range(19)]
dx, dy = [1, 1, 0, -1], [0, 1, 1, 1]
for x in range(19):
    for y in range(19):
        if result[x][y] != 0:
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                cnt = 1
                while 0 <= nx < 19 and 0 <= ny < 19 and result[nx][ny] == result[x][y]:
                    cnt += 1
                    if cnt == 5:
                        if 0 <= x - dx[k] < 19 and 0 <= y - dy[k] < 19 and result[x - dx[k]][y - dy[k]] == result[x][y]:
                            break
                        if 0 <= nx + dx[k] < 19 and 0 <= ny + dy[k] < 19 and result[nx + dx[k]][ny + dy[k]] == result[x][y]:
                            break
                        print(result[x][y])
                        print(x + 1, y + 1)
                        sys.exit(0)
                    nx += dx[k]
                    ny += dy[k]
print(0)
