from collections import deque

T = int(input())
dec = deque()
dec.append(T)
for i in range(T-1, 0, -1):
    dec.appendleft(i)
    for j in range(i):
        temp = dec.pop()
        dec.appendleft(temp)
print(*dec)