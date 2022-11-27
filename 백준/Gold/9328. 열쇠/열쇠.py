from collections import deque
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    matrix = [list('.' * (M+2))] + [list('.' + input().strip() + '.') for _ in range(N)] + [list('.' * (M+2))]
    keys = input().strip()
    key_list = [False] * 26
    if keys != '0':
        for key in keys:
            key_list[ord(key)-97] = True
    for i in range(N+2):
        for j in range(M+2):
            if matrix[i][j].isupper():
                if key_list[ord(matrix[i][j])-65]:
                    matrix[i][j] = '.'
            elif matrix[i][j].islower():
                if key_list[ord(matrix[i][j])-97]:
                    matrix[i][j] = '.'
    dx, dy = [0,0,-1,1], [-1,1,0,0]
    start = deque()
    visited = [[False] * (M+2) for _ in range(N+2)]
    visited[0][0] = True
    start.append((0, 0))
    answer = 0
    while start:
        x, y = start.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N+2 and 0 <= ny < M+2 and not visited[nx][ny]:
                if matrix[nx][ny] == '*':
                    continue
                if matrix[nx][ny] == '.':
                    visited[nx][ny] = True
                    start.append((nx, ny))
                elif matrix[nx][ny].islower():
                    key_list[ord(matrix[nx][ny])-97] = True
                    visited = [[False] * (M+2) for _ in range(N+2)]
                    matrix[nx][ny] = '.'
                    visited[nx][ny] = True
                    start = deque()
                    start.append((nx, ny))
                    break
                elif matrix[nx][ny].isupper():
                    if key_list[ord(matrix[nx][ny])-65]:
                        matrix[nx][ny] = '.'
                        visited[nx][ny] = True
                        start.append((nx, ny))
                else:
                    answer += 1
                    matrix[nx][ny] = '.'
                    visited[nx][ny] = True
                    start.append((nx, ny))
    print(answer)