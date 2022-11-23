from heapq import heappop, heappush
import sys
input = sys.stdin.readline
N = int(input())
start = []
cost_list = []
for i in range(N):
    cost = int(input())
    heappush(start, [cost, i])
    cost_list.append(cost)
woo_list = [list(map(int, input().strip().split())) for _ in range(N)]
visited = [False] * N
result = 0
while start:
    cost, node = heappop(start)
    if not visited[node]:
        visited[node] = True
        result += cost
        for i in range(N):
            if i == node:
                continue
            if cost_list[i] > woo_list[node][i]:
                cost_list[i] = woo_list[node][i]
                heappush(start, [cost_list[i], i])
print(result)