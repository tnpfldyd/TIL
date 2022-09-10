from collections import deque
import sys
input = sys.stdin.readline
N= int(input())
result = [[] for _ in range(N)]
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
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
    cnt = max(visited)
    min_cnt[i+1] = cnt
final = sorted(min_cnt.items(), key = lambda x : (x[1], x[0]))
cnt = 0
result = []
for k, v in final:
    if v == final[0][1]:
        cnt += 1
        result.append(k)
print(final[0][1], cnt)
print(*result)