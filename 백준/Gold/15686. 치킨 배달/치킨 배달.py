import sys, itertools
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
matrix = [list(map(int, input().strip().split())) for _ in range(N)]
house, chicken = [], []
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 0:
            continue
        elif matrix[i][j] == 1:
            house.append((i, j))
        elif matrix[i][j] == 2:
            chicken.append((i, j))
answer = INF
for i in itertools.combinations(chicken, M):
    visited = [INF] * len(house)
    for j in i:
        for idx, location in enumerate(house):
            visited[idx] = min(visited[idx], abs(j[0]-location[0]) + abs(j[1]-location[1]))
    answer = min(answer, sum(visited))
print(answer)