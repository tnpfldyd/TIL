from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    s, e = map(int, input().split())
    start = deque()
    start.append((s, ''))
    visited = [False] * 10000
    visited[s] = True

    while start:
        cur, path = start.popleft()
        if cur == e:
            print(path)
            break
        check = [
            ((cur * 2) % 10000, 'D'),
            ((cur - 1) % 10000, 'S'),
            ((cur * 10 + (cur // 1000)) % 10000, 'L'),
            ((cur // 10 + (cur % 10) * 1000) % 10000, 'R')
            ]
        for nxt, dir in check:
            if not visited[nxt]:
                visited[nxt] = True
                start.append((nxt, path + dir))
