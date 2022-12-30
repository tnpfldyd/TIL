from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N = int(input())

meeting = []
for _ in range(N):
    a, b = map(int, input().split())
    heappush(meeting, (b, a))

result = []
while meeting:
    end, start = heappop(meeting)
    if not result:
        result.append((start, end))
        continue
    if result[-1][1] <= start:
        result.append((start, end))
print(len(result))