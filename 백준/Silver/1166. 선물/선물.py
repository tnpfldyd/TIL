import sys
input = sys.stdin.readline

N, L, W, H = map(int, input().split())

def can_fit(a):
    return (L // a) * (W // a) * (H // a) >= N

left, right = 0, min(L, W, H)

for _ in range(10000):
    mid = (left + right) / 2
    if can_fit(mid):
        left = mid
    else:
        right = mid
print(left)