from heapq import heappop, heappush
import sys

input = sys.stdin.readline
N = int(input())
pq = []
for _ in range(N):
    s, e = map(int, input().split())
    heappush(pq, (s, e))

seat = []
chair = []
computer = []
cnt = 0
while pq:
    s, e = heappop(pq)
    while seat and seat[0][0] < s:
        _, num = heappop(seat)
        heappush(chair, num)
    if not chair:
        heappush(seat, (e, cnt))
        computer.append(1)
        cnt += 1
    else:
        num = heappop(chair)
        heappush(seat, (e, num))
        computer[num] += 1
print(cnt)
print(*computer)