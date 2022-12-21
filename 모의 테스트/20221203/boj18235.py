from collections import deque
import sys
input = sys.stdin.readline
N, o, u = map(int, input().split())
start = deque()
result = set()
start.append((o, 1, 'o')); start.append((u, 1, 'u'))
cntt = 0
while start:
    for i in range(len(start)):
        x, cnt, name = start.popleft()
        if name == 'o':
            for j in (-cnt, cnt):
                nx = x + j
                if 0 < nx <= N:
                    start.append((nx, cnt*2, name))
                    result.add(nx)
        else:
            for j in (-cnt, cnt):
                nx = x + j
                if 0 < nx <= N:
                    if nx in result:
                        print(cntt+1)
                        sys.exit()
                    else:
                        start.append((nx, cnt*2, name))
    result = set()
    cntt += 1
print(-1)