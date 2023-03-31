import sys, math
input = sys.stdin.readline
N = int(input())
all = 1
numbers = []
for i in range(N):
    numbers.append(input().strip())
    all *= (i + 1)
K = int(input())
cache = [1 % K] * 51

for i in range(1, 51):
    cache[i] = (cache[i-1] * 10) % K

cal = []
for i in range(N):
    ret = 0
    for j in range(len(numbers[i])):
        ret *= 10
        ret += int(numbers[i][j])
        ret %= K
    cal.append(ret)
dp = [[0] * (K + 1) for _ in range(1 << N)]
dp[0][0] = 1
for i in range(1 << N):
    for j in range(N):
        if not (i & (1 << j)):
            nxt = i | (1 << j)
            for k in range(K):
                nxtK = ((k * cache[len(numbers[j])]) % K + cal[j]) % K
                dp[nxt][nxtK] += dp[i][k]

cnt = dp[(1 << N) - 1][0]
gcd = math.gcd(all, cnt)
all //= gcd; cnt //= gcd
print(str(cnt) + '/' + str(all))