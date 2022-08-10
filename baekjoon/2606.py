import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
N += 1

matrix = [[] for _ in range(N)] # 리스트 생성
for _ in range(M):
    v1, v2 = map(int, input().rstrip().split())
    matrix[v1].append(v2)
    matrix[v2].append(v1)
visited = [False] * N
stack = [1]
visited[1] = True

while stack:
    virus = stack.pop()
    for i in matrix[virus]:
        if not visited[i]:
            visited[i] = True
            stack.append(i)
print(sum(visited) - 1)
