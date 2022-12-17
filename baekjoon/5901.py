from heapq import heappop, heappush
import sys, itertools
input = sys.stdin.readline
INF = sys.maxsize
N, M, K = map(int, input().split())
k_list = []
k_temp = set()
for i in range(K):
    k = int(input())-1
    k_list.append((i, k))
    k_temp.add(k)
matrix = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((t, b))
    matrix[b].append((t, a))
def heap(s):
    start = []
    heappush(start, [0, s])
    visited = [INF] * N
    visited[s] = 0
    while start:
        cost, node = heappop(start)
        if cost > visited[node]:
            continue
        for k, v in matrix[node]:
            nx = k + cost
            if visited[v] > nx:
                visited[v] = nx
                heappush(start, [nx, v])
    return visited
visit_list = []
for i in k_list:
    visit_list.append(heap(i[1]))
result = INF
for i in range(N):
    if i in k_temp:
        continue
    for j in itertools.permutations(k_list, K):
        cnt = 0
        temp = i
        for k, v in j:
            cnt += visit_list[k][temp]
            temp = v
        cnt += visit_list[j[-1][0]][i]
        if result > cnt:
            result = cnt
print(result)