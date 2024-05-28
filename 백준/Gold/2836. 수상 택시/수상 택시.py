import sys
input = sys.stdin.readline

N, M = map(int, input().split())
points = []

for _ in range(N):
    a, b = map(int, input().split())
    if a <= b:
        continue
    points.append((b, a))

points.sort()

result = 0
if points:
    last = points[0][1]
    result = last - points[0][0]
    for i in range(1, len(points)):
        e, s = points[i]
        if last < e:
            result += s - e
            last = s
        else:
            if last < s:
                result += s - last
                last = s

print(M + result * 2)
