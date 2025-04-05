from collections import deque

N, K, M = map(int, input().split())
queue = deque(range(1, N+1))
direction = 1
removed_count = 0

while queue:
    if direction == 1:
        queue.rotate(-(K - 1))
        print(queue.popleft())
    else:
        queue.rotate(K)
        print(queue.popleft())
    removed_count += 1
    if removed_count % M == 0:
        direction *= -1