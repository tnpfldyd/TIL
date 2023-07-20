from heapq import heappop, heapify

N = int(input())
arr = list(map(int, input().split()))
heapify(arr)

result = 1
while arr:
    x = heappop(arr)
    if result < x:
        break
    result += x
print(result)