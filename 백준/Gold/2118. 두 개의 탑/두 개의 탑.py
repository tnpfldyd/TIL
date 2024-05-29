import sys
input = sys.stdin.readline

N = int(input().strip())
D = [int(input().strip()) for _ in range(N)]

l, r = 0, 1
t = sum(D)
answer = 0
cur = sum([D[0], D[1]])

for _ in range(50001):
    answer = max(answer, min(cur, t - cur))
    if cur >= t - cur:
        cur -= D[l]
        l = (l + 1) % N
    else:
        r = (r + 1) % N
        cur += D[r]

print(answer)
