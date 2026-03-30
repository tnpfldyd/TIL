import sys
input = sys.stdin.readline

n = int(input())
cnt = {}

for _ in range(n):
    c = input().strip()[0]
    cnt[c] = cnt.get(c, 0) + 1

ans = []

for k in sorted(cnt):
    if cnt[k] >= 5:
        ans.append(k)

print(''.join(ans) if ans else 'PREDAJA')