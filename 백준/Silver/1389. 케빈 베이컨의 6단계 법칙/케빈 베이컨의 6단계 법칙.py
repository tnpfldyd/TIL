from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
result = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    result[a-1].append(b-1)
    result[b-1].append(a-1)
min_cnt = {}
for i in range(N):
    visited = [0] * N
    start = deque()
    start.append(i)
    visited[i] = '0'
    while start:
        x = start.popleft()
        for k in result[x]:
            if not visited[k]:
                visited[k] = int(visited[x]) + 1
                start.append(k)
    visited[i] = 0
    cnt = sum(visited)
    min_cnt[i+1] = cnt
final = sorted(min_cnt.items(), key = lambda x : (x[1], x[0]))
print(final[0][0])