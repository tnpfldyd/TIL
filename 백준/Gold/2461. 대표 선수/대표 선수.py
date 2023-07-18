from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = [sorted(map(int, input().split()), reverse=True) for _ in range(N)]


result = float('inf')
minNum = float('inf')
pq = []

for i in range(N):
    minNum = min(minNum, numbers[i][0])
    heappush(pq, (-numbers[i][0], i, 0))

while pq:
    num, idx, arrIdx = heappop(pq)
    num = -num

    result = min(result, num - minNum)

    if arrIdx + 1 == M:
        break

    minNum = min(minNum, numbers[idx][arrIdx + 1])
    heappush(pq, (-numbers[idx][arrIdx + 1], idx, arrIdx + 1))

print(result)