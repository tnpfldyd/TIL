import heapq, sys
input = sys.stdin.readline
T = int(input())
result = []
for i in range(T):
    number = int(input())
    if number != 0:
        heapq.heappush(result, (abs(number), number))
    else:
        if result:
            print(heapq.heappop(result)[1])
        else:
            print(0)