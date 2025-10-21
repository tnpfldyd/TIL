import sys
input = sys.stdin.readline

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

total = 0
for i in range(N):
    pos_i, color_i = points[i]
    min_dist = float('inf')
    
    for j in range(N):
        if i == j:
            continue
        pos_j, color_j = points[j]
        
        if color_i == color_j:
            dist = abs(pos_i - pos_j)
            if dist < min_dist:
                min_dist = dist
    
    total += min_dist

print(total)