import sys
sys.setrecursionlimit(10**6)

MOD = 1000000007
DP = {}

def solution(s, a, b, c):
    if s == 0:
        if a == 0 and b == 0 and c == 0:
            return 1
        else:
            return 0
    
    if (s, a, b, c) in DP:
        return DP[(s, a, b, c)]
    
    res = 0
    if a > 0:
        res += solution(s - 1, a - 1, b, c)
    if b > 0:
        res += solution(s - 1, a, b - 1, c)
    if c > 0:
        res += solution(s - 1, a, b, c - 1)
    if a > 0 and b > 0:
        res += solution(s - 1, a - 1, b - 1, c)
    if a > 0 and c > 0:
        res += solution(s - 1, a - 1, b, c - 1)
    if b > 0 and c > 0:
        res += solution(s - 1, a, b - 1, c - 1)
    if a > 0 and b > 0 and c > 0:
        res += solution(s - 1, a - 1, b - 1, c - 1)
    
    res %= MOD
    DP[(s, a, b, c)] = res
    return res

s, a, b, c = map(int, input().split())
print(solution(s, a, b, c))