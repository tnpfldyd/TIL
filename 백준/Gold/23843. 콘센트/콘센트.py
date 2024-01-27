from heapq import heappop, heappush

N, M = map(int, input().split())
times = list(map(int, input().split()))

times.sort(reverse=True)
pq = []

for i in range(min(N, M)):
    heappush(pq, times[i])

for i in range(M, N):
    min_time = heappop(pq)
    heappush(pq, times[i] + min_time)

result = max(pq)
print(result)