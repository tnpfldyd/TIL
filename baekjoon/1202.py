import sys, heapq
input = sys.stdin.readline
 
N, K = map(int, input().split())
jewelry = []
for i in range(N):
    weight, value = map(int, input().split())
    jewelry.append((weight, value))
bag = []
for i in range(K):
    weight = int(input())
    bag.append(weight)
 
pq = []
 
jewelry.sort()
bag.sort()
 
result = 0
idx = 0

for i in range(K):

    while idx < N and jewelry[idx][0] <= bag[i]:
        heapq.heappush(pq, -jewelry[idx][1])
        idx += 1
 
    if pq:
        result += -heapq.heappop(pq)
 
print(result)