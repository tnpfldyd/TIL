# 순서대로 타겟을 바꿔가며 찾는 방법
from collections import deque
import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(N)]
visited = [[[-1] * (K+1) for _ in range(M)] for _ in range(N)]
start = deque()
a, b = 0, 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 'S':
            start.append((i, j, 0)) # 현재 찾은 타겟이 없기에 위치 i, j 와 0을 덱에 넣기
            visited[i][j][0] = 0
        elif matrix[i][j] == str(K): # 최종 목적지 저장
            a, b = i, j
target = 1 # 1~K 순으로 찾아야 하기에 첫 타겟을 설정
dx, dy = [0,0,1,-1],[1,-1,0,0]
while start:
    x, y, z = start.popleft()
    if x == a and y == b and z == K: # 현재 x,y가 최종 목적지고, 현재 찾은 숫자와 도착 숫자가 같을 때 종료
        print(visited[x][y][z])
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if matrix[nx][ny] != 'X' and matrix[nx][ny] != str(target) and visited[nx][ny][z] == -1: # 벽과 현재 찾는 타겟이 아닐 경우
                visited[nx][ny][z] = visited[x][y][z] + 1
                start.append((nx, ny, z))
            elif matrix[nx][ny] == str(target) and z + 1 == target and visited[nx][ny][z + 1] == -1: # 숫자일때 현재 내가 찾는 타겟 일 경우
                target += 1 # 현재 원하는 타겟은 찾았으니 다음 타겟으로 변경
                visited[nx][ny][z+1] = visited[x][y][z] + 1 
                start = deque() # 덱의 특성상 타겟을 찾았으면 기존에 덱에 있는 애들은 필요가 없어짐. 찾은 애가 가장 빨리 도착했으므로,
                start.append((nx, ny, z+1))
                break
