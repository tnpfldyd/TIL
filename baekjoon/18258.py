from collections import deque
import sys
input = sys.stdin.readline
T = int(input())
dec = deque()
for i in range(T):
    command = input().rstrip().split()
    if command[0] == 'push':
        dec.append(command[1])
    elif command[0] == 'pop':
        print(dec.popleft() if len(dec) != 0 else -1)
    elif command[0] == 'size':
        print(len(dec))
    elif command[0] == 'empty':
        print(0 if len(dec) != 0 else 1)
    elif command[0] == 'front':
        print(dec[0] if len(dec) != 0 else -1)
    elif command[0] == 'back':
        print(dec[-1] if len(dec) != 0 else -1)