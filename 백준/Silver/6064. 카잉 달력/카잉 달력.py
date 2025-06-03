import sys, math
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    g = math.gcd(M, N)
    l = M * N // g

    k = -1
    cur = x
    while cur <= l:
        if (cur - y) % N == 0:
            k = cur
            break
        cur += M

    print(k)