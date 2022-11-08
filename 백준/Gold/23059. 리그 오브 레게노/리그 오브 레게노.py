import sys
input = sys.stdin.readline
N = int(input())
item = {}
rev_item = {}
cnt = 0
temp = []
for i in range(N):
    a, b = input().split()
    if a not in item:
        item[a] = cnt
        rev_item[cnt] = a
        cnt += 1
    if b not in item:
        item[b] = cnt
        rev_item[cnt] = b
        cnt += 1
    temp.append((a, b))
visited = [0] * len(item)
visit = [0] * len(item)
matrix = [[] for _ in range(len(item))]
for k, v in temp:
    matrix[item[k]].append(item[v])
    visited[item[v]] += 1
    visit[item[v]] += 1
start = []
for i in range(len(item)):
    if not visited[i]:
        start.append(rev_item[i])
start.sort(reverse=True)
result = []
temp = []
while start:
    name = start.pop()
    result.append(name)
    for i in matrix[item[name]]:
        visited[i] -= 1
        if visited[i] == 0:
            temp.append(rev_item[i])
    if not start:
        start = temp
        start.sort(reverse=True)
        temp = []
if len(result) == len(item):
    for i in result:
        print(i)
else:
    print(-1)