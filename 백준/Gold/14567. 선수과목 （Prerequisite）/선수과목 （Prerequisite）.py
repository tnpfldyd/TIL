from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

vistied = [0] * (N + 1)
matrix = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    matrix[a].append(b)
    vistied[b] += 1

pq = deque()

for i in range(1, N + 1):
    if not vistied[i]:
        pq.append(i)
result = [0] * (N + 1)
cnt = 1
while pq:
    for _ in range(len(pq)):
        x = pq.popleft()
        result[x] = cnt
        for i in matrix[x]:
            vistied[i] -= 1
            if not vistied[i]:
                pq.append(i)
    cnt += 1
print(*result[1:])