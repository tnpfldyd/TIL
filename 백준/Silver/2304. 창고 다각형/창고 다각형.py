import sys
input = sys.stdin.readline

N = int(input())
pillars = []
for _ in range(N):
    L, H = map(int, input().split())
    pillars.append((L, H))

pillars.sort()

max_pos = max(p[0] for p in pillars)
heights = [0] * (max_pos + 1)
for L, H in pillars:
    heights[L] = H

max_height = max(heights)
max_idx = heights.index(max_height)

left_area = 0
current_height = 0
for i in range(max_idx):
    current_height = max(current_height, heights[i])
    left_area += current_height

right_area = 0
current_height = 0
for i in range(max_pos, max_idx, -1):
    current_height = max(current_height, heights[i])
    right_area += current_height

total_area = left_area + max_height + right_area

print(total_area)