from collections import deque
N = int(input())
deq = deque()
for i in range(1, N+1):
    deq.append(i)
while deq:
    a = deq.popleft()
    if len(deq) == 0:
        print(a)
        break
    b = deq.popleft()
    deq.append(b)