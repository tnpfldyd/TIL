from heapq import heappop, heappush
import sys
dic = {}
rev_dic = {}
input = sys.stdin.readline
N = int(input())
cnt = 0
temp = []
for _ in range(N):
    a, dir, b = input().strip().split()
    if a not in dic:
        dic[a] = cnt
        rev_dic[cnt] = a
        cnt += 1
    if b not in dic:
        dic[b] = cnt
        rev_dic[cnt] = b
        cnt += 1
    temp.append((a, dir, b))
visited = [0] * len(dic)
matrix = [[] for _ in range(len(dic))]
for a, dir, b in temp:
    if dir == '>':
        matrix[dic[a]].append(dic[b])
        visited[dic[b]] += 1
    else:
        matrix[dic[b]].append(dic[a])
        visited[dic[a]] += 1
start = []
for i in range(len(visited)):
    if not visited[i]:
        heappush(start, i)
result = []
while start:
    x = heappop(start)
    result.append(x)
    for k in matrix[x]:
        visited[k] -= 1
        if not visited[k]:
            heappush(start, k)
print('possible' if len(result) == len(dic) else 'impossible')