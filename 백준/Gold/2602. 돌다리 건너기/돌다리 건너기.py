def solve(now_idx, now_b, sq_idx):
    if sq_idx == len(n):
        return 1

    if dp[now_idx][now_b][sq_idx] != -1:
        return dp[now_idx][now_b][sq_idx]

    ret = 0

    for i in range(now_idx, len(bridge[0])):
        if bridge[now_b][i] == n[sq_idx]:
            ret += solve(i + 1, 1 - now_b, sq_idx + 1)

    dp[now_idx][now_b][sq_idx] = ret
    return ret

n = input().strip()
bridge = [input().strip(), input().strip()]

dp = [[[-1 for _ in range(len(n) + 1)] for _ in range(2)] for _ in range(len(bridge[0]) + 1)]

result = solve(0, 0, 0) + solve(0, 1, 0)
print(result)
