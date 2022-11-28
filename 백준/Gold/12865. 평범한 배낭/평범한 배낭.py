import sys
input = sys.stdin.readline
N, K = map(int, input().split())
items = [[0, 0]]+ [list(map(int, input().split())) for _ in range(N)]
bags = [[0] * (K+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, K+1):
        weight = items[i][0]
        happy = items[i][1]
        if j < weight:
            bags[i][j] = bags[i-1][j]
        else:
            bags[i][j] = max(bags[i-1][j], bags[i-1][j-weight] + happy)
print(bags[N][K])