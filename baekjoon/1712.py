A, B, C = list(map(int, input().split()))
if B >= C:
    print(-1)
else:
    print(A // (C-B) + 1)