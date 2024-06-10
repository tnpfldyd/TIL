import sys, math, itertools

input = sys.stdin.readline
INF = sys.maxsize

T = int(input())
results = []

for _ in range(T):
    N = int(input())
    coordinates = []
    total_x, total_y = 0, 0
    
    for _ in range(N):
        x, y = map(int, input().split())
        total_x += x
        total_y += y
        coordinates.append([x, y])
    
    min_diff = INF
    half_combinations = itertools.combinations(coordinates, N // 2)
    
    for group1 in half_combinations:
        group1 = list(group1)
        group1_x, group1_y = 0, 0
        
        for x, y in group1:
            group1_x += x
            group1_y += y
        
        group2_x = total_x - group1_x
        group2_y = total_y - group1_y
        
        diff = math.sqrt((group1_x - group2_x) ** 2 + (group1_y - group2_y) ** 2)
        min_diff = min(min_diff, diff)
    
    results.append(min_diff)

for result in results:
    print(f"{result:.6f}")
