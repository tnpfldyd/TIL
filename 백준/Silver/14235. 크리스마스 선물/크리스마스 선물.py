import heapq
import sys
input = sys.stdin.readline

n = int(input())
gifts = []
result = []

for _ in range(n):
    visit = list(map(int, input().split()))
    a = visit[0]
    
    if a > 0:
        for value in visit[1:]:
            heapq.heappush(gifts, -value)
    else:
        if gifts:
            result.append(-heapq.heappop(gifts))
        else:
            result.append(-1)

for value in result:
    print(value)