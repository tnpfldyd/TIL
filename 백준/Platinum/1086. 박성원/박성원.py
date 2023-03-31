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

pair = []
for i in range(N):
    numbers[i] = numbers[i][::-1]
    sum_ = 0
    for j in range(len(numbers[i])):
        sum_ += int(numbers[i][j]) * cache[j] % K
    pair.append((sum_ % K, len(numbers[i])))
dp = [[-1] * (K + 1) for _ in range(1 << N)]

def dfs(res, num):
    if res == (1 << N) - 1:
        return num % K == 0
    ret = dp[res][num]
    if ret != -1:
        return ret
    ret = 0
    for i in range(N):
        if res & (1 << i):
            continue
        nxt, cnt = pair[i]
        nxtNum = (num * cache[cnt] + nxt) % K
        ret += dfs(res | (1 << i), nxtNum)
    dp[res][num] = ret
    return ret

cnt = dfs(0, 0)
gcd = math.gcd(all, cnt)
all //= gcd; cnt //= gcd

print(str(cnt) + '/' + str(all))