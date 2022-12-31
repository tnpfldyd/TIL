from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
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
            x, node = heappop(start)
            if x > visited[node]:
                continue
            for k, v in matrix[node]:
                nx = x + k
                if visited[v] > nx:
                    visited[v] = nx
                    heappush(start, [nx, v])
        return visited
    person = int(input())
    result = []
    per_num = list(map(int, input().rstrip().split()))
    for i in per_num:
        result.append(heap(i-1))
    min_cnt = [INF, 0]
    for k in range(N):
        cnt = 0
        for i in range(person):
            cnt += result[i][k]
        if min_cnt[0] > cnt:
            min_cnt[0] = cnt
            min_cnt[1] = k
    print(min_cnt[1] + 1)