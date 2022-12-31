T = int(input())
for i in range(1, T+1):
    a, b, c = map(int, input().split())
    D, H, M = a - 11, b - 11, c - 11
    H += (D * 24); M += (H * 60)
    if M < 0:
        M = -1
    print(f'#{i} {M}')