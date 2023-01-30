from collections import deque
import sys
input = sys.stdin.readline
K = int(input())
N, M = map(int, input().split())
matrix = [list(map(int, input().rstrip().split())) for _ in range(M)]
visited = [[[-1] * (K+1) for _ in range(N)] for _ in range(M)] # K번 만큼 이동할 수 있기에
visited[0][0][0] = 0 # (0, 0) 위치에서 말처럼 이동한 횟수가 아직은 0회이기에
start = deque()
start.append((0, 0, 0))
dx, dy = [0,0,-1,1], [-1,1,0,0] # 원숭이처럼 이동할 때
sx, sy = [2,1,2,1,-1,-2,-2,-1],[1,2,-1,-2,-2,-1,1,2] # 말처럼 이동할 때
while start:
    x, y, k = start.popleft()
    if x == M-1 and y == N-1:
        print(visited[x][y][k])
        break
    if k < K: # 아직 총 K 이동횟수 보다 적을 땐 말처럼 이동한 경우와 일반 이동 둘 다 사용 if elif 가 아니라 if if로 둘 다 실행되도록 이동해야함. 
        for i in range(8):
            nx, ny = x + sx[i], y + sy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if visited[nx][ny][k+1] == -1 and matrix[nx][ny] == 0:
                    visited[nx][ny][k+1] = visited[x][y][k] + 1
                    start.append((nx, ny, k+1))
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if visited[nx][ny][k] == -1 and matrix[nx][ny] == 0:
                visited[nx][ny][k] = visited[x][y][k] + 1
                start.append((nx, ny, k))
else:
    print(-1)