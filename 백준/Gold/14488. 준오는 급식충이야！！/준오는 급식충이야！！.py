n, t = map(float, input().split())
x = list(map(float, input().split()))
v = list(map(float, input().split()))

MIN_RANGE = float('inf')
MAX_RANGE = float('-inf')

for i in range(int(n)):
    MIN_RANGE = min(MIN_RANGE, round((x[i] + v[i] * t), 4))
    MAX_RANGE = max(MAX_RANGE, round((x[i] - v[i] * t), 4))

print(1 if MIN_RANGE >= MAX_RANGE else 0)
