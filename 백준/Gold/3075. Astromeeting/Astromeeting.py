import sys
input = sys.stdin.readline
INF = sys.maxsize
T = int(input())
for q in range(T):
    n, N, M = map(int, input().split())
    people = []
    for _ in range(n):
        num = int(input()) - 1
        people.append(num)
    matrix = [[INF] * N for _ in range(N)]
    for _ in range(M):
        a, b, t = map(int, input().split())
        a -= 1; b -= 1
        matrix[a][b] = min(t, matrix[a][b])
        matrix[b][a] = min(t, matrix[b][a])
    for i in range(N):
        matrix[i][i] = 0
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
    number = 0
    min_load = INF
    for k in range(N):
        cnt = 0
        for i in people:
            cnt += matrix[i][k]**2
        if min_load > cnt:
            min_load = cnt
            number = k
    print(number+1, min_load)