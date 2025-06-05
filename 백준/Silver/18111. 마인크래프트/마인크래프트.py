import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(N)]

best_time = float('inf')
best_height = 0

for H in range(257):
    time_spent = 0
    inventory = B
    for i in range(N):
        for j in range(M):
            h = land[i][j]
            if h > H:
                removed = h - H
                time_spent += removed * 2
                inventory += removed
            elif h < H:
                needed = H - h
                time_spent += needed
                inventory -= needed
    if inventory < 0:
        continue
    if time_spent < best_time or (time_spent == best_time and H > best_height):
        best_time = time_spent
        best_height = H

print(best_time, best_height)