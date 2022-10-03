from heapq import heappop, heappush
import sys
input = sys.stdin.readline
T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    time = list(map(int, input().strip().split()))
    matrix = [[] for _ in range(N)]
    visited = [0] * N
    times = [0] * N
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1; b -= 1
        matrix[a].append(b)
        visited[b] += 1
    end = int(input())
    end -= 1
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
    print(times[end])