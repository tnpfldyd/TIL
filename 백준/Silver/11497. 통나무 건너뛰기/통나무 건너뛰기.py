import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    logs = list(map(int, input().split()))
    
    logs.sort()
    
    result = [0] * N
    left = 0
    right = N - 1
    
    for i in range(N):
        if i % 2 == 0:
            result[left] = logs[i]
            left += 1
        else:
            result[right] = logs[i]
            right -= 1
    
    max_diff = 0
    for i in range(N):
        diff = abs(result[i] - result[(i + 1) % N])
        max_diff = max(max_diff, diff)
    
    print(max_diff)