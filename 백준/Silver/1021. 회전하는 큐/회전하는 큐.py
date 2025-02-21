from collections import deque

N, M = map(int, input().split())
targets = list(map(int, input().split()))
queue = deque(range(1, N + 1))
operations = 0

for target in targets:
    while True:
        if queue[0] == target:
            queue.popleft()
            break
        else:
            idx = queue.index(target)
            if idx <= len(queue) // 2:
                queue.rotate(-1)
                operations += 1
            else:
                queue.rotate(1)
                operations += 1

print(operations)