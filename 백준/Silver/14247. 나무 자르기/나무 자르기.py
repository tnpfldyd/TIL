import sys
input = sys.stdin.readline

n = int(input())
h = list(map(int, input().split()))
a = list(map(int, input().split()))

idx = sorted(range(n), key=lambda x: a[x])

ans = 0
for t, i in enumerate(idx, 1):
    ans += h[i] + (t - 1) * a[i]

print(ans)