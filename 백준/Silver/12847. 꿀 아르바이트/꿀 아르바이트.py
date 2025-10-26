import sys
input = sys.stdin.readline

n, m = map(int, input().split())
wages = list(map(int, input().split()))

if m == 0:
    print(0)
else:
    current_sum = sum(wages[:m])
    max_sum = current_sum
    
    for i in range(m, n):
        current_sum = current_sum - wages[i - m] + wages[i]
        max_sum = max(max_sum, current_sum)
    
    print(max_sum)