
k = 300
limits = [2000, 1000, 3000, 200, 600, 500]
sockets = [[2,3,-1,-1,-1],[4,0,-1,-1,6],[5,0,0,0,0],[-1,0,0,0,0],[-1,-1,-1,-1,-1],[-1,-1,0,0,0]]
from collections import deque
matrix = [[] for _ in range(len(limits))]
rev_matrix = [[] for _ in range(len(limits))]
visited = [0] * len(limits)
result = 0
for idx, cost in enumerate(sockets):
    cnt = 0
    for i in cost:
        if i > 1:
            matrix[idx].append(i-1)
            rev_matrix[i-1].append(idx)
        if i == -1:
            cnt += 1
    visited[idx] = cnt * k
    while visited[idx] > limits[idx]:
        visited[idx] -= k
        result += 1
dic = {}
print(visited)
for idx, node in enumerate(matrix):
    dic[idx] = visited[idx] 
    start = deque()
    start.append(idx)
    visit = [False] * len(limits)
    visit[idx] = True
    while start:
        x = start.popleft()
        for i in matrix[x]:
            if not visit[i]:
                visit[i] = True
                dic[idx] += visited[i]
                start.append(i)
print(dic)
dic = dic.items()
dic = sorted(dic, key= lambda x : x[1])
print(dic)
for idx, cost in dic:
    while limits[idx] < cost:
        cost -= k
        result += 1
# print(result)