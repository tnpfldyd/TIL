from collections import deque
import sys
input = sys.stdin.readline
case = int(input())
for _ in range(case):
    N, M = map(int, input().split())
    matrix = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1; b -= 1
        matrix[a].append(b)
        matrix[b].append(a)
    visited = [0] * N
    answer = True
    for i in range(N):
        if visited[i] == 0:
            start = deque()
            start.append(i)
            visited[i] = 1
            while start:
                x = start.popleft()
                for j in matrix[x]:
                    if visited[j] == 0:
                        if visited[x] == 1:
                            visited[j] = 2
                            start.append(j)
                        elif visited[x] == 2:
                            visited[j] = 1
                            start.append(j)
                    if visited[j] != 0:
                        if visited[j] == visited[x]:
                            answer = False
    print('YES' if answer else 'NO')