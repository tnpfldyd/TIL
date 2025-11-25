import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    l, n = map(int, input().split())
    
    min_time = 0
    max_time = 0
    
    for _ in range(n):
        pos = int(input())
        
        min_time = max(min_time, min(pos, l - pos))
        max_time = max(max_time, max(pos, l - pos))
    
    print(min_time, max_time)