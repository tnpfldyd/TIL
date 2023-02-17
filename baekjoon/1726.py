from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]
sx, sy, sd = map(int, input().split()) # 시작 x, y, 방향
ex, ey, ed = map(int, input().split()) # 도착 x, y, 방향
sx -= 1; sy -= 1; sd -= 1; ex -= 1; ey -= 1; ed -= 1
dx, dy = [0,0,1,-1], [1,-1,0,0]
visited = [[[-1] * 4 for _ in range(M)] for _ in range(N)] # 현재 어느 방향인지 까지 동시에 저장해야 하기 때문에 3차원으로 관리.
visited[sx][sy][sd] = 0
start = deque()
start.append((sx, sy, sd))
while start:
    x, y, d = start.popleft()
    if x == ex and y == ey and d == ed:
        print(visited[x][y][d])
        break
    for i in range(1, 4):
        nx, ny = x + (dx[d] * i), y + (dy[d] * i) # 현재 방향으로 1, 2, 3 칸 이동했을때의 경우 문제에 Go k: k는 1, 2, 3 일수 있다 라는 조건
        if nx < 0 or nx >= N or ny < 0 or ny >= M: # 범위를 벗어나거나
            break
        if matrix[nx][ny] == 1: # 벽에 만나면 어짜피 다음 칸으로 갈 수 없기에 break
            break
        if visited[nx][ny][d] == -1:
            visited[nx][ny][d] = visited[x][y][d] + 1
            start.append((nx, ny, d))
    if d > 1: # 현재 방향이 남이나 북일 경우에는 동서로만 방향 변경이 가능함
        for i in range(2):
            if visited[x][y][i] == -1: # 방향 변경하려는 곳이 들린적이 없을때
                visited[x][y][i] = visited[x][y][d] + 1 # 방향 변경하는 것도 카운트 해야하므로 카운트
                start.append((x, y, i))
    if d <= 1: # 현재 방향이 동이나 서일 경우에는 북남으로만 방향 변경이 가능함
        for i in range(2,4):
            if visited[x][y][i] == -1:
                visited[x][y][i] = visited[x][y][d] + 1
                start.append((x, y, i))