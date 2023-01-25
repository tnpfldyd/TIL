from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [[0] * N for _ in range(N)]
union, start = deque(), deque()
for i in range(1, M+1):
    x, y = map(int, input().split())
    x -= 1; y -= 1
    union.append((x, y, i))
    matrix[x][y] = i
parent = [i for i in range(M+1)]
total = [1 for _ in range(M+1)]
dx, dy = [0,0,1,-1],[1,-1,0,0]

def merge_root(a, b):
    pa, pb = find(a, 0), find(b, 0)
    if pa > pb:
        parent[pa] = pb
        find(pa, 0)
    else:
        parent[pb] = pa
        find(pb, 0)
    return

def find(x, x_num):
    if x == parent[x]:
        total[x] += x_num
        return x
    next_x_num = total[x] + x_num
    total[x] = 0
    parent[x] = find(parent[x], next_x_num)
    return parent[x]

def merge():
    while union:
        x, y, cur = union.popleft()
        start.append((x, y, cur))

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                num = matrix[nx][ny]
                if num and cur != num:
                    merge_root(cur, num)                 
cnt = 0
merge()
while total[1] != M:
    cnt += 1
    while start:
        x, y, cur = start.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not matrix[nx][ny]:
                matrix[nx][ny] = cur
                union.append((nx, ny, cur))
    merge()
print(cnt)