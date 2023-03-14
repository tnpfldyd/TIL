import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(input().strip()) for _ in range(N)]

def search():
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 'S':
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < N and 0 <= ny < M:
                        if matrix[nx][ny] == 'W':
                            return False
                        elif matrix[nx][ny] == '.':
                            matrix[nx][ny] = 'D'
    return True

result = search()
if not result:
    print(0)
else:
    print(1)
    for i in matrix:
        print(''.join(i))