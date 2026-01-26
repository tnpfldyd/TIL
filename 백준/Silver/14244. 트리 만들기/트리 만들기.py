n, m = map(int, input().split())

for i in range(n - m):
    print(i, i + 1)

for i in range(n - m + 1, n):
    print(0, i)