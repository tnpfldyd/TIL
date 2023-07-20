import sys
INF = sys.maxsize
input = sys.stdin.readline

def get_max_num(cur):
    if not cur:
        return
    if cur == 3:
        answer.append(7)
        return
    answer.append(1)
    get_max_num(cur - 2)

min_num = [0, 0, 1, 7, 4, 2, 0, 8]

dp = [INF] * 101
dp[2:8] = [1, 7, 4, 2, 6, 8]
for i in range(8, 101):
    for j in range(2, 8):
        dp[i] = min(dp[i], dp[i - j] * 10 + min_num[j])

T = int(input())

for _ in range(T):
    N = int(input())
    answer = []
    get_max_num(N)
    answer = ''.join(map(str, reversed(answer)))
    print(dp[N], answer)