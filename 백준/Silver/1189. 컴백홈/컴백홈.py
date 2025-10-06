import sys
input = sys.stdin.readline

R, C, K = map(int, input().split())
grid = [input().strip() for _ in range(R)]

visited = [[False] * C for _ in range(R)]
count = 0

def backtrack(r, c, dist):
    global count
    
    if r == 0 and c == C - 1:
        if dist == K:
            count += 1
        return
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and grid[nr][nc] == '.':
            visited[nr][nc] = True
            backtrack(nr, nc, dist + 1)
            visited[nr][nc] = False

visited[R - 1][0] = True
backtrack(R - 1, 0, 1)
print(count)