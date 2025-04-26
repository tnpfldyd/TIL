from collections import deque

N = int(input())
dq = deque(range(1, N + 1))

for i in range(1, N):
    p = (i ** 3 - 1) % (N - i + 1)
    dq.rotate(-p)
    dq.popleft()

print(dq[0])