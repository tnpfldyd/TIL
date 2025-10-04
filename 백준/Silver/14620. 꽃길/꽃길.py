import sys
input = sys.stdin.readline

N = int(input())
garden = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]
directions = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]

def get_cost(r, c):
    cost = 0
    for dr, dc in directions:
        cost += garden[r + dr][c + dc]
    return cost

def can_plant(r, c):
    if r < 1 or r >= N - 1 or c < 1 or c >= N - 1:
        return False
    for dr, dc in directions:
        if visited[r + dr][c + dc]:
            return False
    return True

def plant(r, c, value):
    for dr, dc in directions:
        visited[r + dr][c + dc] = value

def solve(count, total_cost):
    global min_cost
    
    if count == 3:
        min_cost = min(min_cost, total_cost)
        return
    
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if can_plant(i, j):
                cost = get_cost(i, j)
                plant(i, j, True)
                solve(count + 1, total_cost + cost)
                plant(i, j, False)

min_cost = float('inf')
solve(0, 0)
print(min_cost)