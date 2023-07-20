from collections import deque
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
Student = [''] + [input().strip() for _ in range(N)]

answer = 0
Q = [deque() for _ in range(25)]
for i in range(1, N+1):
    length = len(Student[i])
    while Q[length] and i - Q[length][0] > K:
        Q[length].popleft()
    answer += len(Q[length])
    Q[length].append(i)
print(answer)
