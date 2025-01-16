import sys
input = sys.stdin.readline

t = int(input())

fibo_dp = [0] * 10000
fibo_dp[0] = 1
fibo_dp[1] = 1
fibo_dp[2] = 2

for i in range(3, 10000):
    fibo_dp[i] = fibo_dp[i-1] + fibo_dp[i-2]


for j in range(t):
    p, q = map(int, input().split())

    print("Case #{}:".format(j+1), (fibo_dp[p-1] % q))