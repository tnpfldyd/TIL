from collections import deque
A, B = map(int, input().split())
start = deque()
start.append((A, 1))
while start:
    X, cnt = start.popleft()
    if X > B:
        continue
    if X == B:
        print(cnt)
        break
    start.append((int(str(X)+'1'), cnt+1))
    start.append((X*2, cnt+1))
else:
    print(-1)
