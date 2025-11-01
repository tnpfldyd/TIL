import sys
input = sys.stdin.readline

N, K = map(int, input().split())
kits = list(map(int, input().split()))

count = 0

def backtrack(day, current_weight, used):
    global count
    
    if day == N:
        count += 1
        return
    
    for i in range(N):
        if used & (1 << i):
            continue
        
        new_weight = current_weight + kits[i]
        
        if new_weight < 500:
            continue
        
        weight_after_day = new_weight - K
        
        if weight_after_day < 500:
            continue
        
        backtrack(day + 1, weight_after_day, used | (1 << i))

backtrack(0, 500, 0)
print(count)