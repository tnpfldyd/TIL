from heapq import heappop,heappush
import sys
INF = sys.maxsize
input = sys.stdin.readline
case = int(input())
for _ in range(case):
    N, M, T = map(int, input().split()) #정점, 간선, 목적지 후보의 갯수
    s1, n1, n2 = map(int, input().split()) # 시작위치, 거쳐야하는 두 정점
    s1 -= 1; n1 -= 1; n2 -= 1
    matrix = [[] for _ in range(N)]
    for _ in range(M):
        a, b, t = map(int, input().split())
        a -= 1; b -= 1
        matrix[a].append((t, b))
        matrix[b].append((t, a)) # 양방향 간선
    def heap(s):
        start = []
        heappush(start, (0, s))
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
                    heappush(start, (nx, v))
        return visited
    answer = heap(s1) # 출발지로부터 출발
    answer1 = heap(n1) # 거쳐야할 정점 1
    answer2 = heap(n2) # 거쳐야할 정점 2
    result = []
    for i in range(T): # T의 갯수 만큼 목적지 인풋
        end = int(input())
        end -= 1
        # 만약 출발지 부터 도착지의 거리와, 두 정점을 거치더라도 거리가 같다면 출 > n1 > n2 > 도 or 출 > n2 > n1 > 도라면 결과에 추가
        if answer[end] == answer[n1] + answer1[n2] + answer2[end] or answer[end] == answer[n2] + answer2[n1] + answer1[end]:
            result.append(end+1)
    result.sort()
    print(*result)
