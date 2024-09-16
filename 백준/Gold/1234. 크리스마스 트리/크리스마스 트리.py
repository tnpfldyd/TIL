import sys
sys.setrecursionlimit(10 ** 6)

N, R, G, B = map(int, input().split())

cache = [[[[-1 for _ in range(60)] for _ in range(60)] for _ in range(60)] for _ in range(11)]
fact = [0] * 11

def getFacto(n):
    if n == 0 or n == 1:
        return 1
    if fact[n]:
        return fact[n]
    fact[n] = n * getFacto(n-1)
    return fact[n]

def numCase(facto, r, g, b):
    return facto // getFacto(r) // getFacto(g) // getFacto(b)

def dfs(lv, r, g, b):
    if lv > N:
        return 1
    
    if cache[lv][r][g][b] != -1:
        return cache[lv][r][g][b]
    
    ret = 0

    if R - r >= lv:
        ret += dfs(lv+1, r+lv, g, b)
    if G - g >= lv:
        ret += dfs(lv+1, r, g+lv, b)
    if B - b >= lv:
        ret += dfs(lv+1, r, g, b+lv)

    if lv % 2 == 0:
        if R - r >= lv//2 and G - g >= lv//2:
            ret += (numCase(getFacto(lv), lv//2, lv//2, 0) * dfs(lv+1, r+lv//2, g+lv//2, b))
        if B - b >= lv//2 and G - g >= lv//2:
            ret += (numCase(getFacto(lv), 0, lv//2, lv//2) * dfs(lv+1, r, g+lv//2, b+lv//2))
        if R - r >= lv//2 and B - b >= lv//2:
            ret += (numCase(getFacto(lv), lv//2, 0, lv//2) * dfs(lv+1, r+lv//2, g, b+lv//2))

    if lv % 3 == 0 and R - r >= lv//3 and G - g >= lv//3 and B - b >= lv//3:
        ret += (numCase(getFacto(lv), lv//3, lv//3, lv//3) * dfs(lv+1, r+lv//3, g+lv//3, b+lv//3))
    
    cache[lv][r][g][b] = ret
    return ret

print(dfs(1, 0, 0, 0))