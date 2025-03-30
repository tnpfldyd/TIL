import sys
input = sys.stdin.readline

while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    
    sang = set()
    for _ in range(N):
        sang.add(int(input()))
    
    count = 0
    for _ in range(M):
        if int(input()) in sang:
            count += 1
    
    print(count)