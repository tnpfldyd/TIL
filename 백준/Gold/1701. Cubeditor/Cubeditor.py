def kmp(p):
    n = len(p)
    ret = 0
    fail = [0] * n
    j = 0

    for i in range(1, n):
        while j > 0 and p[i] != p[j]:
            j = fail[j - 1]
        if p[i] == p[j]:
            ret = max(ret, j + 1)
            j += 1
            fail[i] = j

    return ret

p = input()
N = len(p)
result = 0

for i in range(N):
    result = max(result, kmp(p[i:]))

print(result)