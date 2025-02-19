import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
dq = deque()

for _ in range(n):
    command = input().split()
    if command[0] == 'push_front':
        dq.appendleft(int(command[1]))
    elif command[0] == 'push_back':
        dq.append(int(command[1]))
    elif command[0] == 'pop_front':
        print(dq.popleft() if dq else -1)
    elif command[0] == 'pop_back':
        print(dq.pop() if dq else -1)
    elif command[0] == 'size':
        print(len(dq))
    elif command[0] == 'empty':
        print(1 if not dq else 0)
    elif command[0] == 'front':
        print(dq[0] if dq else -1)
    elif command[0] == 'back':
        print(dq[-1] if dq else -1)