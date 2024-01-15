S = input()
t = input()
dp = [0] * (len(t) + 1)
dp[0] = float("inf")

find_idx = {a:idx + 1 for idx, a in enumerate(t)}

for s in S:
    if s in find_idx and dp[find_idx[s] - 1] > dp[find_idx[s]]:
        dp[find_idx[s]] += 1

print(dp[-1])