import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
start = tuple(map(int, input().split()))
target = tuple(sorted(start))

visited = set()
queue = deque()
queue.append((start, 0))
visited.add(start)

while queue:
    current, depth = queue.popleft()
    if current == target:
        print(depth)
        break
    for i in range(N - K + 1):
        next_perm = list(current)
        next_perm[i:i+K] = reversed(next_perm[i:i+K])
        next_tuple = tuple(next_perm)
        if next_tuple not in visited:
            visited.add(next_tuple)
            queue.append((next_tuple, depth + 1))
else:
    print(-1)