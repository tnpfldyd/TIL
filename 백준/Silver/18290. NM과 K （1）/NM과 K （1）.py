import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]
max_sum = float('-inf')

def is_adjacent(r, c):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M and visited[nr][nc]:
            return True
    return False

def backtrack(idx, count, total):
    global max_sum
    
    if count == K:
        max_sum = max(max_sum, total)
        return
    
    if idx >= N * M:
        return
    
    r, c = idx // M, idx % M
    
    if not visited[r][c] and not is_adjacent(r, c):
        visited[r][c] = True
        backtrack(idx + 1, count + 1, total + grid[r][c])
        visited[r][c] = False
    
    backtrack(idx + 1, count, total)

backtrack(0, 0, 0)
print(max_sum)