import heapq, sys
input = sys.stdin.readline
T = int(input())
result = []
for i in range(T):
    number = int(input())
    heapq.heappush(result, number)
for j in range(len(result)):
    print(heapq.heappop(result))