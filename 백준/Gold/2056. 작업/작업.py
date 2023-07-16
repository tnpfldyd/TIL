from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

indegree = [0] * (N + 1)
time = [0] * (N + 1)
dp = [0] * (N + 1)
matrix = [[] for _ in range(N + 1)]

for i in range(1, N + 1):
    cost, *num = list(map(int, input().split()))
    time[i] = cost
    indegree[i] = num[0]
    for j in range(1, num[0] + 1):
        matrix[num[j]].append(i)

q = deque()
for i in range(1, N + 1):
    if not indegree[i]:
        q.append(i)
        dp[i] = time[i]

result = 0

for _ in range(N):
    if not q:
        break
    x = q.popleft()
    result = max(result, dp[x])
    for y in matrix[x]:
        dp[y] = max(dp[y], dp[x] + time[y])
        indegree[y] -= 1
        if not indegree[y]:
            q.append(y)

print(result)