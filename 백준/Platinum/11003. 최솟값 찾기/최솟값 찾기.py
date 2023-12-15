from collections import deque
N, L = map(int,input().split())
numbers = list(map(int, input().split()))
q = deque()

for i in range(N):
    number = numbers[i]
    if q and q[0][0] <= i - L:
        q.popleft()

    while q and number < q[-1][1]:
        q.pop()

    q.append((i, number))
    
    print(q[0][1], end = " ")