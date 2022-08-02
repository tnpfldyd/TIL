import heapq, sys
input = sys.stdin.readline
numbers = []
T = int(input())
for i in range(T):
    number = int(input())
    if number == 0:
        if numbers:
            print(heapq.heappop(numbers))
        else:
            print(0)
    else:
        heapq.heappush(numbers, number)
