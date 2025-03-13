from collections import deque

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

queue_values = deque()
for i in range(N):
    if A[i] == 0:
        queue_values.appendleft(B[i])

results = []
for c in C:
    if queue_values:
        results.append(queue_values.popleft())
        queue_values.append(c)
    else:
        results.append(c)

print(" ".join(map(str, results)))