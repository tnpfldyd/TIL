import sys
input = sys.stdin.readline

N, L = map(int, input().split())
coords = sorted(list(map(int, input().split())) for _ in range(N))

cnt = 0
cur = 0
for s, e in coords:
    if s > cur:
        cur = s
    while cur < e:
        cur += L
        cnt += 1

print(cnt)