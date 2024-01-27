import sys
input = sys.stdin.readline

N = int(input())
names = [int(input()) for _ in range(N)]

count = [0] * 20
total = 0

for name in names:
    for i in range(20):
        if name & (1 << i):
            count[i] += 1

for i, c in enumerate(count):
    total += c * (N - c) * (1 << i)

print(total)