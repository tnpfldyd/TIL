import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
occupied = set()

for _ in range(Q):
    x = int(input())
    cur = x
    blocked = 0
    
    while cur:
        if cur in occupied:
            blocked = cur
        cur //= 2
    
    print(blocked)
    if blocked == 0:
        occupied.add(x)