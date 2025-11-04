import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

N, M = map(int, input().split())
points = list(map(int, input().split()))

points.sort()

for _ in range(M):
    start, end = map(int, input().split())
    
    left_idx = bisect_left(points, start)
    right_idx = bisect_right(points, end)
    
    print(right_idx - left_idx)