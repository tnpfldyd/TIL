from heapq import heappop, heappush
import sys
input = sys.stdin.readline

graph = []
point = []
visit = [False] * 100001
bitidx = [0] * 100001
dist = [[-1 for _ in range(22)] for _ in range(22)]
distmp = [0] * 100001
dp = [[0 for _ in range(1 << 22)] for _ in range(22)]

def dijkstra(start):
    global dist, visit, distmp
    visit = [False] * 100001
    distmp = [-1] * 100001
    q = []
    heappush(q, (0, start))
    distmp[start] = 0

    while q:
        cost, cur = heappop(q)
        if visit[cur]:
            continue
        visit[cur] = True
        if bitidx[cur] > -1:
            dist[bitidx[start]][bitidx[cur]] = cost
        for dst, weight in graph[cur]:
            if distmp[dst] == -1 or distmp[dst] > distmp[cur] + weight:
                distmp[dst] = distmp[cur] + weight
                heappush(q, (distmp[dst], dst))

def go(idx, bit):
    global dp, dist, bitidx, point
    if idx == z:
        if bit == (1 << (p + 2)) - 1:
            return 0
        else:
            return -1

    if dp[bitidx[idx]][bit] != 0:
        return dp[bitidx[idx]][bit]

    ret = -1
    for i in range(len(point)):
        dst = point[i]
        if dist[bitidx[idx]][bitidx[dst]] == -1:
            continue

        next_bit = bit | (1 << bitidx[dst])

        if next_bit == bit:
            continue

        tmp = go(dst, next_bit)
        if tmp < 0:
            continue

        if ret == -1 or ret > tmp + dist[bitidx[idx]][bitidx[dst]]:
            ret = tmp + dist[bitidx[idx]][bitidx[dst]]

    dp[bitidx[idx]][bit] = ret
    return ret

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dist = [[-1 for _ in range(22)] for _ in range(22)]
bitidx = [-1] * 100001
dp = [[0 for _ in range(1 << 22)] for _ in range(22)]
visit = [False] * 100001
point = []

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

x, z = map(int, input().split())
p = int(input())
bitidx[x] = 0
bitidx[z] = p + 1
point.append(x)
p_list = list(map(int, input().split()))
for i in range(1, p + 1):
    a = p_list[i - 1]
    bitidx[a] = i
    point.append(a)

point.append(z)

for i in range(len(point)):
    dijkstra(point[i])

print(go(x, 1))