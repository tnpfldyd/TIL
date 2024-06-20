import sys
input = sys.stdin.readline
MOD = 1000000007

M = int(input())

def cal(x):
    if x == 1:
        return N
    p = cal(x // 2)
    if not x % 2:
        return (p * p) % MOD
    else:
        return (p * p * N) % MOD

total_count = 0
for _ in range(M):
    N, S = map(int, input().split())
    inverse_n = cal(MOD - 2)
    total_count = (total_count + inverse_n * S) % MOD

print(total_count)