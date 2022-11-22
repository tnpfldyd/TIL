from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
matrix = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((t, b))
    matrix[b].append((t, a))

def heap(user):
    visited = [INF] * N
    visited[user] = 0
    start = []
    dic = {}
    heappush(start, [0, user, []])
    while start:
        x, node, load = heappop(start)
        if x > visited[node]:
            continue
        for cost, next in matrix[node]:
            nx = x + cost
            if visited[next] > nx:
                visited[next] = nx
                dic[(user, next)] = load+[(node, next)]
                heappush(start, [nx, next, load+[(node, next)]])

    return visited, dic
x, y, z = map(int, input().split())
x -= 1; y -= 1; z -= 1
xcost, xload = heap(x)
ycost, yload = heap(y)
zcost, zload = heap(z)
answer = INF
load = []
for i in range(N):
    temp = xcost[i] + ycost[i] + zcost[i]
    if answer > temp:
        answer = temp
        load = []
        tempx = xload.get((x, i))
        tempy = yload.get((y, i))
        tempz = zload.get((z, i))
        if tempx:
            for j in tempx:
                load.append(j)
        if tempy:
            for j in tempy:
                load.append(j)
        if tempz:
            for j in tempz:
                load.append(j)
print(answer, len(load))
for x, y in load:
    print(x + 1, y + 1)