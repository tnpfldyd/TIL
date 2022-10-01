from heapq import heappop, heappush
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
result = []
matrix = [[] for _ in range(N)]
visited = [0] * N
for i in range(M):
    list_ = list(map(int,input().rstrip().split()))
    for j in range(1, list_[0]):
        matrix[list_[j]-1].append(list_[j+1]-1)
        visited[list_[j+1]-1] += 1
start = []
for i in range(N):
    if not visited[i]:
        heappush(start, i)
while start:
    x = heappop(start)
    result.append(x + 1)
    for i in matrix[x]:
        visited[i] -= 1
        if visited[i] == 0:
            heappush(start, i)
if len(result) != N:
    print(0)
else:
    for i in result:
        print(i)