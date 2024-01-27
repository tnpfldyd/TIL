from collections import deque
q = deque()
count = 0
N = int(input())

for i in range(10):
    q.append(i)

while q:
    cur = q.popleft()
    if count == N:
        print(cur)
        break

    for i in range(cur % 10):
        q.append(cur * 10 + i)
    count += 1
else:
    print(-1)