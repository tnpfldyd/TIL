import sys
import math

input = sys.stdin.readline
mod = 10007

def combination(n, k):
    if k > n or k < 0:
        return 0
    return math.comb(n, k) % mod

def Ncard(N):
    result = 0
    for i in range(1, N // 4 + 1):
        result += combination(52 - i * 4, N - i * 4) * combination(13, i) * ((-1) ** (i - 1))
        result %= mod
    return result

print(Ncard(int(input())))