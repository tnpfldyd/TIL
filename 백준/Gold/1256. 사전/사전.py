from math import comb
n, m, k = map(int, input().split())

if comb(n + m, n) < k:
    print(-1)
else:
    result = ""
    while True:
        if not n or not m:
            result += "a" * n
            result += "z" * m
            break
        cases = comb(n + m - 1, n - 1)
        if k > cases:
            result += "z"
            m -= 1
            k -= cases
        else:
            result += "a"
            n -= 1
    print(result)