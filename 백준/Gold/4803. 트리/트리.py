from collections import deque
import sys

input = sys.stdin.readline
con = 0
while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    matrix = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        matrix[a].append(b)
        matrix[b].append(a)
    cnt = 0
    visited = [-1] * N
    for i in range(N):
        if visited[i] == -1:
            answer = True
            start = deque()
            start.append(i)
            while start:
                x = start.popleft()
                if visited[x] != -1:
                    answer = False
                visited[x] = 0
                for j in matrix[x]:
                    if visited[j] == -1:
                        start.append(j)
            if answer:
                cnt += 1
    con += 1
    if cnt == 0:
        print(f"Case {con}: No trees.")
    elif cnt == 1:
        print(f"Case {con}: There is one tree.")
    else:
        print(f"Case {con}: A forest of {cnt} trees.")