import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
for i in range(T):
    N = int(input())
    start1, start2 = map(int, input().split())
    Nresult = []
    for j in range(N):
        x, y = map(int, input().split())
        Nresult.append([x, y])
    final1, final2 = map(int, input().split())
    visited = [0 for _ in range(N+1)]
    dec = deque()
    dec.append((start1, start2))
    while dec:
        a, b = dec.popleft()
        if abs(a - final1) + abs(b - final2) <= 1000:
            print('happy')
            break
        for k in range(N):
            if not visited[k]:
                na, nb = Nresult[k]
                if abs(a - na) + abs(b - nb) <= 1000:
                    dec.append((na, nb))
                    visited[k] = 1
    else:
        print('sad')