import sys
input = sys.stdin.readline

N = int(input())
points = []

for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

ans = 0
min_dist = float('inf')

for i in range(N):
    max_dist = 0
    for j in range(N):
        dist = ((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2) ** 0.5
        max_dist = max(max_dist, dist)
    
    if min_dist > max_dist:
        min_dist = max_dist
        ans = i

print(*points[ans])
