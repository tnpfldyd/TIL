import sys
input = sys.stdin.readline

N = int(input())
v = []

for _ in range(N):
    x, y = map(int, input().split())
    v.append((min(x, y), max(x, y)))

v.sort()
dp = [1] * N
answer = 1

for i in range(N):
    x, y = v[i]
    for j in range(i):
        nx, ny = v[j]
        if x >= nx and y >= ny:
            dp[i] = max(dp[i], dp[j] + 1)
    answer = max(answer, dp[i])

print(answer)