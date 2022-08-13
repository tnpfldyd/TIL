from pprint import pprint
import sys
sys.stdin = open('2628input.txt', 'r')
x, y = map(int, input().split())
T = int(input())
matrix = [[0] * x for _ in range(y)]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1] # 우 하 좌 상
visited = [[False] * x for _ in range(y)]
result = []
for i in range(T):
    direction, number = map(int, input().split())
    if direction == 0:
        for j in range(y):
            for k in range(x):
                if j >= number:
                    matrix[j][k] += 1
    else:
        for j in range(y):
            for k in range(x):
                if k >= number:
                    matrix[j][k] += 1
for j in range(y):
    for k in range(x):
        if not visited[j][k]:
            stack = [(j, k)]
            visited[j][k] = True
            cnt = 1
            while stack:
                wy, wx = stack.pop()
                for n in range(4):
                    nx = wx + dx[n]; ny = wy + dy[n]
                    if 0 <= nx < x and 0 <= ny < y:
                        if not visited[ny][nx] and matrix[j][k] == matrix[ny][nx]:
                            stack.append((ny, nx))
                            cnt += 1
                            visited[ny][nx] = True
            result.append(cnt)
print(max(result))