from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
S = int(input()) - 1
animal = int(input())
A_house = list(map(int, input().strip().split()))
B_house = list(map(int, input().strip().split()))
matrix = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((t, b))
    matrix[b].append((t, a))
visited = [INF] * N
visited[S] = 0
start = []
heappush(start, [0, S])
while start:
    x, node = heappop(start)
    if x > visited[node]:
        continue
    for k, v in matrix[node]:
        nx = x + k
        if visited[v] > nx:
            visited[v] = nx
            heappush(start, [nx, v])
A_min, B_min = INF, INF
for i in A_house:
    if visited[i-1] < A_min:
        A_min = visited[i-1]
for i in B_house:
    if visited[i-1] < B_min:
        B_min = visited[i-1]
if A_min <= B_min and A_min != INF:
    print('A')
    print(A_min)
elif A_min > B_min:
    print('B')
    print(B_min)
else:
    print(-1)