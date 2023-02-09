from heapq import heappop, heappush
import sys
INF = sys.maxsize
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, M, s = map(int, input().split()) # 정점, 간선, 시작노드
    s -= 1
    visited = [INF] * N
    matrix = [[] for _ in range(N)]
    for _ in range(M):
        a, b, t = map(int, input().split())
        a -= 1; b -= 1
        matrix[b].append((t, a)) # b가 감염되면 t초 후에 a가 감염되기 때문에 반대로 간선을 저장
    start = []
    heappush(start, (0, s))
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
    max_cnt = 0
    cnt = 0
    for i in visited:
        if i != INF: # 만약 visited[x] 가 INF 라면 도달하지 못하여 감염시키지 못한 것 이기 때문에, INF 가 아니면 cnt를 ++하고 도달 할 수 있는 최대 시간도 갱신해줌
            cnt += 1
            if max_cnt < i:
                max_cnt = i
    print(cnt, max_cnt)