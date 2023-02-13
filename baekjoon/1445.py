from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M= map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(N)]
visited = [[INF] * M for _ in range(N)] # 쓰레기 옆을 지날 때는 힙에서만 관리하고, 3차원으로 굳이 관리하지 않아도 됨
start = []
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 'S':
            heappush(start, (0, 0, i, j)) # 쓰레기, 쓰레기옆, i, j 순
            visited[i][j] = 0
dx, dy = [0,0,1,-1], [1,-1,0,0]
while start:
    grb, grbs, x, y = heappop(start)
    if matrix[x][y] == 'F':
        print(grb, grbs)
        break
    if grb > visited[x][y]:
        continue
    for k in range(4):
        next_grb, next_grbs, nx, ny = grb, grbs, x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if matrix[nx][ny] == 'g': # 다음 장소가 쓰레기면 next_grb 에 1 추가
                next_grb += 1
            elif matrix[nx][ny] == '.': # 만약 일반 도로면 쓰레기 옆을 지나는지 4방향 탐색
                cnt = 0
                for j in range(4):
                    sx, sy = nx + dx[j], ny + dy[j]
                    if 0 <= sx < N and 0 <= sy < M:
                        if matrix[sx][sy] == 'g':
                            cnt += 1
                if cnt: # 만약 쓰레기 옆을 지난다면 1 추가 쓰레기, 양옆에 있는 쓰레기 2개 사이로 지나더라도 지나는 횟수는 +1 이기때문에 for문 밖에서 실행
                    next_grbs += 1
            if visited[nx][ny] > next_grb:
                visited[nx][ny] = next_grb
                heappush(start, (next_grb, next_grbs, nx, ny))
# 힙의 특성상 맨 앞의 기준으로 정렬하고 만약 맨 앞에 인자가 동일하다면, 두번째 인자의 최소값을 맨 앞으로 당김.
# visited 를 3차원으로 관리하여도 괜찮지만 쓰레기 갯수만 카운팅하고, 2번째 인자는 힙이 자동으로 관리하도록 했음.