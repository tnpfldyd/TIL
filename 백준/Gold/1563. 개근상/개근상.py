def memoized(day, lateness, absent):
    if lateness == 2: return 0
    if absent == 3: return 0
    if day > N: return 1
    
    ret = dp[day][lateness][absent]
    if ret != -1:
        return ret
    
    ret = (memoized(day + 1, lateness, 0) + memoized(day + 1, lateness + 1, 0) + memoized(day + 1, lateness, absent + 1)) % MOD
    dp[day][lateness][absent] = ret
    return ret
MOD = 1_000_000
N = int(input())
dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(N + 1)] 
print(memoized(1, 0, 0))