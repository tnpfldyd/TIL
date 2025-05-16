s, N, K, R1, R2, C1, C2 = map(int, input().split())

def is_black(s, r, c, N, K):
    if s == 0:
        return False
    unit = N ** (s - 1)
    row = r // unit
    col = c // unit
    mid_start = (N - K) // 2
    mid_end = mid_start + K
    if mid_start <= row < mid_end and mid_start <= col < mid_end:
        return True
    return is_black(s - 1, r % unit, c % unit, N, K)

for r in range(R1, R2 + 1):
    line = ''
    for c in range(C1, C2 + 1):
        line += '1' if is_black(s, r, c, N, K) else '0'
    print(line)