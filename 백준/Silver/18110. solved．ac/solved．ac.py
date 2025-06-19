import sys
input = sys.stdin.readline

n = int(input())
if n == 0:
    print(0)
    sys.exit()

a = [int(input()) for _ in range(n)]
a.sort()

k = int(n * 0.15 + 0.5)
b = a[k : n - k]

s = sum(b)
m = len(b)

print(s // m + (1 if (s % m) * 2 >= m else 0))