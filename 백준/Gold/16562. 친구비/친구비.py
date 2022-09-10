from collections import deque
import sys
input = sys.stdin.readline
N, M, money = map(int, input().split())
money_list = list(map(int, input().split()))
matrix = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    matrix[a-1].append(b-1)
    matrix[b-1].append(a-1)
visited = [False] * N
result = []
for i in range(N):
    if not visited[i]:
        min_m = 99999999999
        start = deque()
        start.append(i)
        if money_list[i] < min_m:
            min_m = money_list[i]
        visited[i] = True
        while start:
            x = start.popleft()
            for k in matrix[x]:
                if not visited[k]:
                    visited[k] = True
                    if min_m > money_list[k]:
                        min_m = money_list[k]
                    start.append(k)
        result.append(min_m)
print(sum(result) if sum(result) <= money else 'Oh no')