import sys
input = sys.stdin.readline
N = int(input())
array = list(map(int, input().strip().split()))
dp = [0] * (N + 1)
cnt = [0] * 30

for idx, number in enumerate(array, 1):
    dp[idx] = dp[idx-1] ^ number

for i in range(30):
    for j in range(1, N + 1):
        if dp[j] & 1 << i:
            cnt[i] += 1
answer = 0
for i in range(30):
    answer += (1 << i) * cnt[i] * (N + 1 - cnt[i])
print(answer)