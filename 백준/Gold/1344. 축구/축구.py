N = 19
range_list = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18]
C = [0] * N

def init():
    C[0] = C[1] = 1
    for i in range(2, N):
        C[0] = C[i] = 1
        for j in range(i-1, 0, -1):
            C[j] += C[j-1]

def solve():
    init()
    a, b = int(input()), int(input())
    a /= 100
    b /= 100

    sa = 0
    sb = 0
    for r in range_list:
        sa += C[r] * a ** r * (1 - a) ** (N - 1 - r)
        sb += C[r] * b ** r * (1 - b) ** (N - 1 - r)
    return 1 - sa * sb

print(f"{solve():.6f}")
