from collections import deque
import sys
input = sys.stdin.readline

def print_order(N, M, priorities):
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    order = 0
    
    while queue:
        doc = queue.popleft()
        if any(doc[1] < q[1] for q in queue):
            queue.append(doc)
        else:
            order += 1
            if doc[0] == M:
                return order

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    priorities = list(map(int, input().split()))
    
    print(print_order(N, M, priorities))