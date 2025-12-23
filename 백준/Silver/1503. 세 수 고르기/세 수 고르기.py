import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = set(map(int, input().split())) if M > 0 else set(input())

ans = 10 ** 9
MAX = 1001

for x in range(1, MAX + 1):
    if x in S:
        continue
    for y in range(1, MAX + 1):
        if y in S:
            continue
        for z in range(1, MAX + 1):
            if z in S:
                continue
            val = x * y * z
            if ans > abs(N - val):
                ans = abs(N - val)
            if N < val:
                break

print(ans)