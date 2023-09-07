MAX = 1000000
import sys
input = sys.stdin.readline

sums = [0] * (MAX + 1)

for i in range(1, MAX + 1):
    for j in range(1, (MAX // i) + 1):
        sums[i * j] += i
    sums[i] += sums[i - 1]

T = int(input())
for _ in range(T):
    print(sums[int(input())])