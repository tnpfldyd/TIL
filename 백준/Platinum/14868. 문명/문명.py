from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [[0] * N for _ in range(N)]
union, start = deque(), deque()
for i in range(1, M+1):
    x, y = map(int, input().split())
    x -= 1; y -= 1
    union.append((x, y))
    matrix[x][y] = i
parent = [i for i in range(M+1)]
dx, dy = [0,0,1,-1],[1,-1,0,0]

def merge_root(a, b):
    pa, pb = find(a), find(b)
    if pa != pb:
        parent[pa] = pb

def find(x):
    if x == parent[x]:
        return x
    px = find(parent[x])
    return px

def root(a, b):
    pa, pb = find(a), find(b)
    return pa == pb
def merge():
    global M

    while union:
        x, y = union.popleft()
        start.append((x, y))

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny]:
                if matrix[nx][ny] != matrix[x][y] and not root(matrix[x][y], matrix[nx][ny]):
                    merge_root(matrix[x][y], matrix[nx][ny])
                    M -= 1                    
cnt = 0
while M > 1:
    merge()
    if M == 1:
        print(cnt)
        break
    while start:
        x, y = start.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not matrix[nx][ny]:
                matrix[nx][ny] = matrix[x][y]
                union.append((nx, ny))
    cnt += 1
