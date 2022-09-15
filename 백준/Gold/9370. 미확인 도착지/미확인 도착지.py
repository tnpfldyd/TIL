from heapq import heappop,heappush
import sys
INF = sys.maxsize
input = sys.stdin.readline
case = int(input())
for _ in range(case):
    N, M, T = map(int, input().split())
    s1, n1, n2 = map(int, input().split())
    s1 -= 1; n1 -= 1; n2 -= 1
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
    answer = heap(s1)
    answer1 = heap(n1)
    answer2 = heap(n2)
    result = []
    for i in range(T):
        end = int(input())
        end -= 1
        if answer[end] == answer[n1] + answer1[n2] + answer2[end] or answer[end] == answer[n2] + answer2[n1] + answer1[end]:
            result.append(end+1)
    result.sort()
    print(*result)