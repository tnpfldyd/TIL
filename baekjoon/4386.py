from heapq import heappop, heappush
N = int(input())
temp = []
for i in range(N):
    a, b = map(float, input().split())
    temp.append((a, b))
matrix = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i != j:
            cost = ((temp[i][0]-temp[j][0])**2 + (temp[i][1]-temp[j][1])**2)**0.5
            matrix[i].append((cost, j))
visited = [False] * N
start = []
heappush(start, [0, 0])
result, cnt = 0, 0
while start:
    cost, node = heappop(start)
    if cnt == N:
        break
    if not visited[node]:
        visited[node] = True
        cnt += 1
        result += cost
        for next in matrix[node]:
            heappush(start, next)
print(result)