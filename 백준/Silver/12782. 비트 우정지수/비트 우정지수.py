import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    N, M = input().split()

    a = 0
    b = 0

    for n, m in zip(N, M):
        if n != m:
            if n == '1':
                a += 1
            else:
                b += 1

    print(max(a, b))