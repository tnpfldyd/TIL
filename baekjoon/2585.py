from collections import deque
import sys
input = sys.stdin.readline

def get_oil(x1, y1, x2, y2):
    oil = ((x1-x2) ** 2 + (y1-y2) ** 2) ** 0.5
    if oil % 10:
        return oil // 10 + 1
    return oil // 10

def bfs(mid):
    start = deque()
    start.append((0, 0, 0))
    visited = [False] * (N+1)
    visited[0] = True
    while start:
        x, y, cnt = start.popleft()
        if cnt > K:
            continue
        if mid >= get_oil(x, y, 10000, 10000):
            return True
        for idx, next in enumerate(N_list):
            nx, ny = next
            temp = get_oil(x, y, nx, ny)
            if mid >= temp and not visited[idx]:
                visited[idx] = True
                start.append((nx, ny, cnt+1))
    return False

N, K = map(int, input().split())

N_list = [(0, 0)]

for _ in range(N):
    a, b = map(int, input().split())
    N_list.append((a, b))

left, right = 0, 10000
answer = 0
while left <= right:
    mid = (left + right) // 2
    if bfs(mid):
        right = mid - 1
        answer = mid
    else:
        left = mid + 1
print(answer)