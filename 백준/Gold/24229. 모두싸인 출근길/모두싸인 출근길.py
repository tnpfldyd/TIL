import sys
input = sys.stdin.readline
N = int(input())
points = sorted([tuple(map(int, input().split())) for _ in range(N)])

v = []
left, right = points[0]

for i in range(1, N):
    s, e = points[i]
    if right >= s:
        right = max(right, e)
    else:
        v.append((left, right))
        left, right = s, e

v.append((left, right))

max_right = 0
idx = 0

for i in range(len(v)):
    s, e = v[i]
    if max_right >= s:
        idx = i
        max_right = max(max_right, e + e - s)

print(v[idx][1])