import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

nutrients = [[5] * N for _ in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for _ in range(K):
    dead_trees = [[0] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if trees[i][j]:
                trees[i][j].sort()
                new_trees = []
                for age in trees[i][j]:
                    if nutrients[i][j] >= age:
                        nutrients[i][j] -= age
                        new_trees.append(age + 1)
                    else:
                        dead_trees[i][j] += age // 2
                trees[i][j] = new_trees
    
    for i in range(N):
        for j in range(N):
            nutrients[i][j] += dead_trees[i][j]
    
    for i in range(N):
        for j in range(N):
            for age in trees[i][j]:
                if age % 5 == 0:
                    for d in range(8):
                        ni, nj = i + dx[d], j + dy[d]
                        if 0 <= ni < N and 0 <= nj < N:
                            trees[ni][nj].append(1)
    
    for i in range(N):
        for j in range(N):
            nutrients[i][j] += A[i][j]

answer = sum(sum(len(trees[i][j]) for j in range(N)) for i in range(N))
print(answer)