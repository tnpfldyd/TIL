from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N = int(input())
points = [list(map(int, input().split())) + [i] for i in range(N)]
parents = [i for i in range(N)]
pq = []

def getDistance(x1, y1, x2, y2):
    result = (x1 - x2) ** 2 + (y1 - y2) ** 2
    return result

for i in range(N - 1):
    x1, y1, a = points[i]
    for j in range(i + 1, N):
        x2, y2, b = points[j]
        cost = getDistance(x1, y1, x2, y2)
        heappush(pq, (cost, a, b))

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    x, y = find(a), find(b)
    if x != y:
        parents[y] = x
        return True
    return False

cnt = 0
while pq:
    cost, a, b = heappop(pq)
    if union(a, b):
        cnt += 1
        if cnt == N - 1:
            print(cost)
            break