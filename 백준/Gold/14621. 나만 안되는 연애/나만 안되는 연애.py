from heapq import heappush, heappop
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
list_ = input().rstrip().split()
matrix = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    if list_[a] == list_[b]:
        continue
    matrix[a].append((t, b))
    matrix[b].append((t, a))
visited = [False] * N
start = []
heappush(start, [0, 0])
cnt = 0; temp = 0
while start:
    x, node = heappop(start)
    if temp == N:
        break
    if not visited[node]:
        visited[node] = True
        temp += 1
        cnt += x
        for k, v in matrix[node]:
            heappush(start, (k, v))
print(cnt if temp == N else -1)