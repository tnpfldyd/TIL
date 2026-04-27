import sys
from collections import deque

input = sys.stdin.buffer.readline

n = int(input())
dq = deque()
history = bytearray()

for _ in range(n):
    line = input()
    op = line[0]

    if op == 49:
        dq.append(line[2:3])
        history.append(1)
    elif op == 50:
        dq.appendleft(line[2:3])
        history.append(2)
    else:
        if history:
            if history.pop() == 1:
                dq.pop()
            else:
                dq.popleft()

sys.stdout.buffer.write(b''.join(dq) if dq else b'0')