from heapq import heappop, heappush
import sys
input = sys.stdin.readline
N = int(input())
time = []
matrix = [[] for _ in range(N)]
visited = [0] * N
times = [0] * N
for i in range(N):
    list_ = list(map(int, input().rstrip().split()))
    time.append(list_[0])
    for j in range(1, len(list_)):
        if list_[j] == -1:
            continue
        matrix[list_[j]-1].append(i)
        visited[i] += 1
start = []
for i in range(N):
    if not visited[i]:
        heappush(start, i)
        times[i] = time[i]
while start:
    x = heappop(start)
    for i in matrix[x]:
        visited[i] -= 1
        times[i] = max(times[x] + time[i], times[i])
        if not visited[i]:
            heappush(start, i)
for i in times:
    print(i)