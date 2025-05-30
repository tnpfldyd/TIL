N, r, c = map(int, input().split())

def z_order(N, r, c):
    if N == 0:
        return 0
    half = 2 ** (N - 1)
    if r < half and c < half:
        return z_order(N-1, r, c)
    elif r < half and c >= half:
        return half * half + z_order(N-1, r, c - half)
    elif r >= half and c < half:
        return 2 * half * half + z_order(N-1, r - half, c)
    else:
        return 3 * half * half + z_order(N-1, r - half, c - half)

print(z_order(N, r, c))