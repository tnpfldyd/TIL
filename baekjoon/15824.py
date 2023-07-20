def scoville(n, k):
    ret = 1
    if k == 0:
        return 1
    if k == 1:
        return n
    ret = scoville(n, k // 2)
    ret = (ret * ret) % MOD
    if k % 2:
        ret *= n
    return ret % MOD

MOD = 10**9 + 7
N = int(input())
v = list(map(int, input().split()))
v.sort()
answer = 0
for i in range(N):
    answer += v[i] * (scoville(2, i) + MOD - scoville(2, N - i - 1)) % MOD
    answer %= MOD
print(answer)
