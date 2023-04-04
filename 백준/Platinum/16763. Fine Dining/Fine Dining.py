import heapq, sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
adj = [[] for _ in range(n+1)]
distN = [float('inf')]*(n+1)
ans = [0]*(n+1)
cost = [float('inf')]*(n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a].append((b,c))
    adj[b].append((a,c))

PQ = []
heapq.heappush(PQ, (0, n))
distN[n] = 0
while PQ:
    d, cur = heapq.heappop(PQ)
    if distN[cur] != d:
        continue
    for nxt, nxtd in adj[cur]:
        if distN[nxt] > d+nxtd:
            distN[nxt] = d+nxtd
            heapq.heappush(PQ, (distN[nxt],nxt))

PQ = []
for _ in range(k):
    a, b = map(int, input().split())
    if cost[a] < distN[a]-b:
        continue
    cost[a] = distN[a]-b
    heapq.heappush(PQ, (cost[a],a))

while PQ:
    bb, cur = heapq.heappop(PQ)
    if bb != cost[cur]:
        continue
    if bb <= distN[cur]:
        ans[cur] = 1
    for nxt, nxtd in adj[cur]:
        if cost[nxt] > bb + nxtd:
            cost[nxt] = bb+nxtd
            heapq.heappush(PQ, (cost[nxt],nxt))

for i in range(1, n):
    print(ans[i])