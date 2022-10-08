from collections import deque
import sys
input = sys.stdin.readline
F, S, G, U, D = map(int, input().split())
result = [0] * (F+1)
start = deque()
start.append(S)
result[S] = 1
while start:
    x = start.popleft()
    if x == G:
        print(result[x] - 1)
        break
    for i in (x+U, x-D):
        if 0 < i <= F and result[i] == 0:
            result[i] = result[x] + 1
            start.append(i)
else:
    print('use the stairs')