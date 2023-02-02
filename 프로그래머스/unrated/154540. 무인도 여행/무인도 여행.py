from collections import deque
def solution(maps):
    answer = []
    N, M = len(maps), len(maps[0])
    dx, dy = [0,0,1,-1], [1,-1,0,0]
    visited = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if maps[i][j] != 'X' and not visited[i][j]:
                visited[i][j] = True
                cnt = int(maps[i][j])
                start = deque()
                start.append((i, j))
                while start:
                    x, y = start.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < N and 0 <= ny < M:
                            if maps[nx][ny] != 'X' and not visited[nx][ny]:
                                visited[nx][ny] = True
                                cnt += int(maps[nx][ny])
                                start.append((nx, ny))
                answer.append(cnt)
    answer.sort()
    if not answer:
        answer = [-1]
    return answer