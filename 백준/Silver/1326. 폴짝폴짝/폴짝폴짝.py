import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
stones = [0] + list(map(int, input().split()))
a, b = map(int, input().split())

visited = [False] * (N + 1)
queue = deque([(a, 0)])
visited[a] = True

while queue:
    pos, jumps = queue.popleft()
    
    if pos == b:
        print(jumps)
        exit()
    
    step = stones[pos]
    
    for next_pos in range(pos, N + 1, step):
        if not visited[next_pos]:
            visited[next_pos] = True
            queue.append((next_pos, jumps + 1))
    
    for next_pos in range(pos, 0, -step):
        if not visited[next_pos]:
            visited[next_pos] = True
            queue.append((next_pos, jumps + 1))

print(-1)