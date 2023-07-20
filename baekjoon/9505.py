from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize

T = int(input())

for _ in range(T):

    K, M, N = map(int, input().split())
    K_dic = {}
    K_dic['E'] = INF

    for _ in range(K):
        alpha, time = input().split()
        K_dic[alpha] = int(time)

    matrix = []
    pq = []
    visited = [[INF] * M for _ in range(N)]

    for i in range(N):
        arr = list(map(lambda x : K_dic[x], input().strip()))
        for j in range(M):
            if arr[j] == INF:
                heappush(pq, (0, i, j))
                visited[i][j] = 0
                arr[j] = 0
        matrix.append(arr)

    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    answer = False

    while pq and not answer:
        cost, x, y = heappop(pq)
        if visited[x][y] < cost:
            continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                nxt_cost = cost + matrix[nx][ny]
                if visited[nx][ny] > nxt_cost:
                    visited[nx][ny] = nxt_cost
                    heappush(pq, (nxt_cost, nx, ny))
            else:
                print(cost)
                answer = True