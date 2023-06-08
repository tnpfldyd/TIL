string = '_' + input()
N = len(string)
P = [[False] * (N) for _ in range(N)]

for i in range(1, N):
    P[i][i] = True
for i in range(1, N - 1):
    if string[i] == string[i + 1]:
        P[i][i + 1] = True
for i in range(3, N):
    for s in range(1, N - i + 1):
        e = s + i - 1
        if string[s] == string[e] and P[s + 1][e - 1]:
            P[s][e] = True
INF = 10e9
dp = [INF] * N
dp[0] = 0
for i in range(1, N):
    for j in range(1, i + 1):
        if P[j][i]:
            dp[i] = min(dp[i], dp[j - 1] + 1)
print(dp[N - 1])