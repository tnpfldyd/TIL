from collections import deque
import sys
INF = sys.maxsize
input = sys.stdin.readline

N = int(input())
matrix = []
min_num, max_num = INF, 0
for _ in range(N):
    arr = list(map(int, input().strip().split()))
    for j in arr:
        if j < min_num:
            min_num = j
        if j > max_num:
            max_num = j
    matrix.append(arr)
left, right = 0, max_num-min_num
dx, dy = [0,0,1,-1],[1,-1,0,0]
def bfs(mid):
    for i in range(mid, max_num+1):
        s, e = i - mid, i
        if s <= matrix[0][0] <= e:
            start = deque()
            start.append((0, 0))
            visited = [[False] * N for _ in range(N)]
            visited[0][0] = True
            while start:
                x, y = start.popleft()
                if (x, y) == (N-1, N-1):
                    return True
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                        if s <= matrix[nx][ny] <= e:
                            visited[nx][ny] = True
                            start.append((nx, ny))
    return False
answer = right
while left <= right:
    mid = (left + right) // 2
    if bfs(mid):
        right = mid - 1
        answer = mid
    else:
        left = mid + 1
print(answer)