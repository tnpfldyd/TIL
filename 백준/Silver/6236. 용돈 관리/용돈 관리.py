import sys
input = sys.stdin.readline

def can_manage(k, expenses, n, m):
    count = 1
    current = k
    
    for i in range(n):
        if current < expenses[i]:
            count += 1
            current = k
        current -= expenses[i]
    
    return count <= m

n, m = map(int, input().split())
expenses = [int(input()) for _ in range(n)]

left = max(expenses)
right = sum(expenses)

while left < right:
    mid = (left + right) // 2
    if can_manage(mid, expenses, n, m):
        right = mid
    else:
        left = mid + 1

print(left)