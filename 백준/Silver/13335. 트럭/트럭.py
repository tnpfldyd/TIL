from collections import deque

def solution():
    n, w, L = map(int, input().split())
    trucks = list(map(int, input().split()))
    
    bridge = deque([0] * w)
    waiting = deque(trucks)
    
    time = 0
    current_weight = 0
    
    while waiting or current_weight > 0:
        time += 1
        removed_weight = bridge.popleft()
        current_weight -= removed_weight
        
        if waiting:
            if current_weight + waiting[0] <= L:
                next_truck = waiting.popleft()
                bridge.append(next_truck)
                current_weight += next_truck
            else:
                bridge.append(0)
        else:
            bridge.append(0)
    
    return time

print(solution())