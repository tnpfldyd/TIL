import sys
input = sys.stdin.readline

MOD = 10 ** 9 + 7

def cal(a, b):
    if not b:
        return 1
    elif not b % 2:
        mul = cal(2, b // 2)
        return mul * mul % MOD
    else:
        mul = cal(2, b // 2)
        temp = mul * mul % MOD
        return a * temp % MOD

T = int(input())
for _ in range(T):
    n = int(input())
    if n == 1:
        print(1)
    else:
        print(cal(2, n - 2))