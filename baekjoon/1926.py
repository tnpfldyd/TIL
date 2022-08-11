from pprint import pprint
import sys
sys.stdin = open('1926input.txt', 'r')
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx, dy = [0, 1, 0, -1],[1, 0, -1, 0] # 우 하 좌 상
result = [] # 그림의 넓이 저장
cnt = 0 # 그림의 갯수 저장
for x in range(n):
    for y in range(m):
        if matrix[x][y] == 1 and visited[x][y] == False:
            temp = 1
            cnt += 1
            visited[x][y] = True
            start = [(x, y)]
            while start:
                a, b = start.pop()
                for k in range(4):
                    nx = a + dx[k]
                    ny = b + dy[k]
                    if 0 <= nx < n and 0 <= ny < m:
                        if matrix[nx][ny] == 1 and visited[nx][ny] == False:
                            visited[nx][ny] = True
                            start.append((nx, ny))
                            temp += 1
            result.append(temp)
print(cnt)
if cnt == 0: # 만약 그림이 1개도 없으면 넓이는 0 으로 출력하도록 문제에 명시 됨.
    print(0)
else:
    print(max(result))