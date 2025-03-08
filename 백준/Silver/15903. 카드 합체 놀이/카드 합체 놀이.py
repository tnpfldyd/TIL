import heapq

n, m = map(int, input().split())
cards = list(map(int, input().split()))

heapq.heapify(cards)

for _ in range(m):
    x = heapq.heappop(cards)
    y = heapq.heappop(cards)
    sum_xy = x + y
    heapq.heappush(cards, sum_xy)
    heapq.heappush(cards, sum_xy)

result = sum(cards)
print(result)