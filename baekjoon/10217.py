import sys
input = sys.stdin.readline
INF = sys.maxsize

for _ in range(int(input())):
    ans = INF
    N, M, K = map(int, input().split())
    matrix = [[] for _ in range(N+1)]
    for _ in range(K):
        u, v, c, d = map(int, input().split())
        matrix[u].append((v, c, d))

    dp = [[INF]*(M+1) for _ in range(N+1)]
    dp[1][0] = 0

    for j in range(M+1):
        for i in range(1, N+1):
            if dp[i][j] == INF:
                continue
            t = dp[i][j]
            for nv, nc, nd in matrix[i]:
                if nc+j > M:
                    continue
                dp[nv][nc+j] = min(dp[nv][nc+j], t+nd)

    res = min(dp[N])
    print(res if res != INF else "Poor KCM")