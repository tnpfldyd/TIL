from collections import deque
import sys
input = sys.stdin.readline
S, E = map(int, input().split())
N, M = map(int, input().split())
matrix = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)

visited = set()
q = deque([(S, 0)])
while q:
    x, cnt = q.popleft()
    if x == E:
        print(cnt)
        break
    for nxt in matrix[x]:
        if (x, nxt) not in visited and (nxt, x) not in visited:
            visited.add((x, nxt))
            q.append((nxt, cnt + 1))
else:
    print(-1)