from heapq import heappop, heappush
start = []
heappush(start, [0,0,1])
heappush(start, [0,2,1])
heappush(start, [0,2,2])
heappush(start, [0,1,1])
print(heappop(start))
print(heappop(start))
print(heappop(start))
print(heappop(start))