import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    ranks = [0] * (N + 1)
    [ranks.__setitem__(a, b) for a, b in [map(int, input().split()) for _ in range(N)]]
    top = ranks[1]
    cnt = 1
    for i in range(2, N + 1):
        if top >= ranks[i]:
            top = ranks[i]
            cnt += 1
    print(cnt)