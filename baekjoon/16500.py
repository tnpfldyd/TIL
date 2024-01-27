import sys
input = sys.stdin.readline
S = input().strip()
N = int(input())
A = [input().strip() for _ in range(N)]
dp = [0] * 101

dp[len(S)] = 1

for pos in range(len(S) - 1, -1, -1):
    for j in range(N):
        if S.find(A[j], pos) == pos and dp[pos + len(A[j])] == 1:
            dp[pos] = 1
            break
        else:
            dp[pos] = 0

print(dp[0])