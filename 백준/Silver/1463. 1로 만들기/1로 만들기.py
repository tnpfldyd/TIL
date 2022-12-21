N = int(input())

visited = [0] * (N+1)
for i in range(2, N+1):
    visited[i] = visited[i-1] + 1
    if not i % 2:
        visited[i] = min(visited[i], visited[i//2] + 1)
    if not i % 3:
        visited[i] = min(visited[i], visited[i//3] + 1)
print(visited[N])