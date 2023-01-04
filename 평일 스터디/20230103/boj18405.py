from collections import deque
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]

start = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] != 0:
            start.append((i, j, matrix[i][j])) 
start = deque(sorted(start, key = lambda x : x[2])) # 번호 기준으로 정렬
dx, dy = [-1,1,0,0],[0,0,1,-1]
S, X, Y = map(int, input().split())
check = False
start2 = deque()
for i in range(S):
    if not check:
        while start:
            x, y, z = start.popleft()
            for j in range(4):
                nx, ny = x + dx[j], y + dy[j]
                if 0 <= nx < N and 0 <= ny < N:
                    if matrix[nx][ny] == 0:
                        matrix[nx][ny] = z
                        start2.append((nx, ny, z))
        check = True
    else:
        while start2:
            x, y, z = start2.popleft()
            for j in range(4):
                nx, ny = x + dx[j], y + dy[j]
                if 0 <= nx < N and 0 <= ny < N:
                    if matrix[nx][ny] == 0:
                        matrix[nx][ny] = z
                        start.append((nx, ny, z))
        check = False
print(matrix[X-1][Y-1])

N, K = map(int, input().split())
matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]
start = []

for i in range(N):
    for j in range(N):
        if matrix[i][j] != 0:
            start.append((i, j, matrix[i][j], 0))

start = deque(sorted(start, key = lambda x : x[2]))

dx, dy = [-1,1,0,0],[0,0,1,-1]
S, X, Y = map(int, input().split())

while start:
    x, y, num, cnt = start.popleft()
    if cnt == S:
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if not matrix[nx][ny]:
                matrix[nx][ny] = num
                start.append((nx, ny, num, cnt+1))

print(matrix[X-1][Y-1])


N, K = map(int, input().split())
matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]
start = []

for i in range(N):
    for j in range(N):
        if matrix[i][j] != 0:
            start.append((i, j, matrix[i][j]))

start = deque(sorted(start, key = lambda x : x[2]))

dx, dy = [-1,1,0,0],[0,0,1,-1]
S, X, Y = map(int, input().split())
cnt = 0
while start:
    if cnt == S:
        break
    for _ in range(len(start)):
        x, y, num = start.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not matrix[nx][ny]:
                    matrix[nx][ny] = num
                    start.append((nx, ny, num))
    cnt += 1

print(matrix[X-1][Y-1])

N, K = map(int, input().split())
matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]
start = []

for i in range(N):
    for j in range(N):
        if matrix[i][j] != 0:
            start.append((i, j, matrix[i][j]))

start = deque(sorted(start, key = lambda x : x[2]))

dx, dy = [-1,1,0,0],[0,0,1,-1]
S, X, Y = map(int, input().split())
cnt = 0

for _ in range(S):
    for _ in range(len(start)):
        x, y, num = start.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not matrix[nx][ny]:
                    matrix[nx][ny] = num
                    start.append((nx, ny, num))

print(matrix[X-1][Y-1])