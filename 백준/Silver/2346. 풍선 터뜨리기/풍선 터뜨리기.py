from collections import deque

N = int(input())
numbers = list(map(int, input().split()))

balloons = deque([(i + 1, numbers[i]) for i in range(N)])
result = []

while balloons:
    idx, move = balloons.popleft()
    result.append(idx)
    
    if balloons:
        if move > 0:
            balloons.rotate(-(move - 1))
        else:
            balloons.rotate(-move)

print(*result)