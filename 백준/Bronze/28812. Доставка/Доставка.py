import sys
input = sys.stdin.readline

n, C = map(int, input().split())

min_cost = float('inf')

for _ in range(n):
    p, d, v = map(int, input().split())
    total = p + d + (C * v)
    min_cost = min(min_cost, total)

print(min_cost)