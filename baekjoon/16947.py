from collections import deque
N = int(input())
matrix = [[] for _ in range(N)]
for _ in range(N):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append(b)
    matrix[b].append(a)
answer = [False] * N
for i in range(N):
    start = deque()
    visited = [False] * N
    visited[i] = True
    start.append((i, 0))
    while start:
        x, cnt = start.popleft()
        for k in matrix[x]:
            if not visited[k]:
                visited[k] = True
                start.append((k, cnt+1))
            if k == i:
                print(cnt)
                print('yes')
            
print(answer)