n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]

for point in points:
    point[1] = abs(point[1])

points.sort()
points = [[-float('inf'), -float('inf')]] + points

min_costs = [0] * (n + 1)

for i in range(1, n + 1):
    current_x, current_y = points[i]
    min_costs[i] = min_costs[i - 1] + current_y * 2
    max_height = current_y * 2
    
    for j in range(i - 1, 0, -1):
        prev_x, prev_y = points[j]
        max_height = max(prev_y * 2, max_height)
        max_dimension = max(current_x - prev_x, max_height)
        min_costs[i] = min(min_costs[i], min_costs[j - 1] + max_dimension)

print(min_costs[n])