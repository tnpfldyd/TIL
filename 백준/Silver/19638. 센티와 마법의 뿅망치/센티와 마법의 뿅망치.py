import sys
import heapq

input = sys.stdin.readline

n, h_centi, t = map(int, input().split())
giants = [-int(input()) for _ in range(n)]
heapq.heapify(giants)

count = 0

while t > 0:
    tallest = -heapq.heappop(giants)

    if tallest < h_centi:
        heapq.heappush(giants, -tallest)
        break

    if tallest == 1:
        heapq.heappush(giants, -1)
        break

    new_height = tallest // 2
    heapq.heappush(giants, -new_height)

    count += 1
    t -= 1

if -giants[0] < h_centi:
    print("YES")
    print(count)
else:
    print("NO")
    print(-giants[0])