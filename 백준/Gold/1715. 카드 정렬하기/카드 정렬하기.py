from heapq import heappop, heappush
import sys
input = sys.stdin.readline
N = int(input())
result = []
cnt = 0
for _ in range(N):
    heappush(result, int(input()))
while len(result) > 1:
    temp1 = heappop(result); temp2 = heappop(result)
    cnt += temp1+temp2
    heappush(result, temp1+temp2)
print(cnt)