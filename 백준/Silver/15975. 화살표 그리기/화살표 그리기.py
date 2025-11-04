import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
points = []
for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

color_dict = {}
for x, y in points:
    if y not in color_dict:
        color_dict[y] = []
    color_dict[y].append(x)

for color in color_dict:
    color_dict[color].sort()

total = 0
for x, y in points:
    coords = color_dict[y]
    
    if len(coords) == 1:
        continue
    
    idx = bisect_left(coords, x)
    
    min_dist = float('inf')
    
    if idx > 0:
        min_dist = min(min_dist, x - coords[idx - 1])
    
    if idx < len(coords) - 1:
        min_dist = min(min_dist, coords[idx + 1] - x)
    
    total += min_dist

print(total)