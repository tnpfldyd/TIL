import sys
input = sys.stdin.readline
L, N, RF, RB = map(int, input().split())
v = []

for _ in range(N):
    x, c = map(int, input().split())
    v.append((c, x))

v.sort(reverse=True)

current = 0
answer = 0

for i in range(N):
    a, b = v[i]
    if current < b:
        answer += (RF - RB) * (b - current) * a
        current = b

print(answer)