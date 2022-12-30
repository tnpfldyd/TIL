from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
N_dic, M_dic = {}, {}
visited = [-1] * 101
for i in range(N):
    a, b = map(int, input().split())
    N_dic[a] = b
for i in  range(M):
    a, b = map(int, input().split())
    M_dic[a] = b
visited[1] = 0

start = deque()
start.append(1)
while start:
    x = start.popleft()
    if x == 100:
        print(visited[x])
        break
    for i in range(1, 7):
        nx = x + i
        if 0 <= nx < 101 and visited[nx] == -1:
            if N_dic.get(nx):
                nx = N_dic[nx]
                if visited[nx] == -1:
                    visited[nx] = visited[x] + 1
                    start.append(nx)
            elif M_dic.get(nx):
                nx = M_dic[nx]
                if visited[nx] == -1:
                    visited[nx] = visited[x] + 1
                    start.append(nx)
            else:
                visited[nx] = visited[x] + 1
                start.append(nx)