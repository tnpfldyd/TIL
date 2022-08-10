import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
N += 1
matrix = [[] for _ in range(N)]
for _ in range(M):
    num, edge = map(int, input().rstrip().split())
    matrix[num].append(edge)
    matrix[edge].append(num)
visited = [False] * N
cnt = 0
for j in range(1, N):
    if not visited[j]:
        stack = [j]
        visited[j] = True
        while stack:
            virus = stack.pop()
            for i in matrix[virus]:
                if not visited[i]:
                    visited[i] = True
                    stack.append(i)
        cnt += 1
print(cnt)
