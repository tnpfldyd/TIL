from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
N *= 24
score = list(map(int,input().split()))
extra = list(map(int,input().split()))
pq = []
for i in range(M):
    if score[i] + extra[i] > 100:
        extra[i] = 100 - score[i]
    heappush(pq,(-extra[i], score[i]))

time = 0
while time < N:
    p, s = heappop(pq)
    s -= p
    if s - p > 100:
        p = s - 100
    heappush(pq, (p, s))
    time += 1
answer = 0
while pq:
    p, s = heappop(pq)
    answer += s
print(answer)