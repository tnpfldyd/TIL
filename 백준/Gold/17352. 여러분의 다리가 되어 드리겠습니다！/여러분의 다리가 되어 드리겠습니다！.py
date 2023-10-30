from collections import deque
import sys
inpurt = sys.stdin.readline

N = int(input())
matrix = [[] for _ in range(N + 1)]

for _ in range(N - 2):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)

q = deque([1])
visited = [False] * (N + 1)
visited[1] = True

while q:
    x = q.popleft()
    for next_ in matrix[x]:
        if not visited[next_]:
            visited[next_] = True
            q.append(next_)

for i in range(1, N + 1):
    if not visited[i]:
        print(1, i)
        break