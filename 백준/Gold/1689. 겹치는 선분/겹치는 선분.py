import sys
input = sys.stdin.readline

N = int(input())
points = []
for _ in range(N):
    s, e = map(int, input().split())
    points.append((s, 1))
    points.append((e, -1))

points.sort()

answer = 0
cnt = 0
for point in points:
    cnt += point[1]
    answer = max(answer, cnt)

print(answer)