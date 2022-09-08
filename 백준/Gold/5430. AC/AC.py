from collections import deque
import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    command = input().strip()
    A = int(input())
    text = deque(input().strip()[1:-1].split(','))
    cnt = 0
    for i in command:
        if i == 'R':
            cnt += 1
        else:
            if len(text) >= 1:
                if text == deque(['']):
                    print('error')
                    break
                elif len(text) > 0:
                    if cnt % 2 == 0:
                        text.popleft()
                    else:
                        text.pop()
            else:
                print('error')
                break
    else:
        if cnt % 2 == 1:
            text.reverse()
        print('['+",".join(text)+']')