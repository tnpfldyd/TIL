from collections import deque
import sys
input = sys.stdin.readline
T = int(input())
dec = deque()
for i in range(T):
    Text = input().rstrip().split()
    if Text[0] == 'push':
        dec.append(Text[1])
    elif Text[0] == 'pop':
        if len(dec) > 0:
            print(dec.popleft())
        else:
            print(-1)
    elif Text[0] == 'size':
        print(len(dec))
    elif Text[0] == 'empty':
        if len(dec) > 0:
            print(0)
        else:
            print(1)
    elif Text[0] == 'front':
        if len(dec) > 0:
            print(dec[0])
        else:
            print(-1)
    else:
        if len(dec) > 0:
            print(dec[-1])
        else:
            print(-1)