from collections import deque
import sys
input = sys.stdin.readline
T = int(input())
matrix = list(map(int, input().split()))
new_matrix = [[] for _ in range(T)]
visited = [False] * T
qw = int(input())

start = deque()
for i in range(T):
    if i == qw:
        continue
    if matrix[i] != -1:
        new_matrix[matrix[i]].append(i)
    else:
        start.append(i)
        visited[i] = True    
cnt = 0
while start:
    x = start.popleft()
    temp = len(start)
    for i in new_matrix[x]:
        if not visited[i]:
            visited[i] = True
            start.append(i)
    temp2 = len(start)
    if temp == temp2:
        cnt += 1
print(cnt)