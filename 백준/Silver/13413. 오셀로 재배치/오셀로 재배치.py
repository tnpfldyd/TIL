import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    initial = input().strip()
    target = input().strip()
    
    wb_count = 0
    bw_count = 0
    
    for i in range(N):
        if initial[i] == 'W' and target[i] == 'B':
            wb_count += 1
        elif initial[i] == 'B' and target[i] == 'W':
            bw_count += 1
    
    swap = min(wb_count, bw_count)
    flip = abs(wb_count - bw_count)
    
    print(swap + flip)