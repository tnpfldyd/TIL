import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    perm = [0] + list(map(int, input().split()))
    visited = [False] * (N + 1)
    cycle_count = 0

    for i in range(1, N + 1):
        if not visited[i]:
            cycle_count += 1
            x = i
            while not visited[x]:
                visited[x] = True
                x = perm[x]
    
    print(cycle_count)