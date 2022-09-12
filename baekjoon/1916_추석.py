# 시간 초과
# import sys
# input = sys.stdin.readline
# INF = sys.maxsize
# T = int(input())
# matrix = [[INF] * (T) for _ in range(T)]
# M = int(input())
# for i in range(M):
#     x, y, k = map(int, input().split())
#     matrix[x-1][y-1] = min(matrix[x-1][y-1], k)
# for i in range(T):
#     matrix[i][i] = 0
# for k in range(T):
#     for a in range(T):
#         for b in range(T):
#             matrix[a][b] = min(matrix[a][b], matrix[a][k] + matrix[k][b])
# start, end = map(int, input().split())
# print(matrix[start-1][end-1])
from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
T = int(input())
M = int(input())
matrix = [[] for _ in range(T)]
for i in range(M):
    a, b, k = map(int, input().split()) 
    matrix[a-1].append([b-1, k])
start, end = map(int, input().split())
visited = [INF] * T
stack = []
heappush(stack, [0, start-1])
visited[start-1] = 0
while stack:
    cost, x = heappop(stack)
    if cost > visited[x]:
        continue
    else:
        for i in matrix[x]:
            temp = cost + i[1]
            if visited[i[0]] > temp:
                visited[i[0]] = temp
                heappush(stack, [temp, i[0]])
print(visited[end-1])