import sys
input = sys.stdin.readline

N, M = int(input()), int(input())

v = sorted([tuple(map(int, input().split())) for _ in range(M)])
l = v[0][0] if v else 0
r = v[0][1] if v else 0
result = l

for i in range(1, M):
    s, e = v[i]
    if s <= r:
        r = max(r, e)
    else:
        result += s - r
        l, r = s, e

result += N - r

print(result)
