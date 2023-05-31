import sys
input = sys.stdin.readline
N = int(input())
sums = []
diffs = []

for _ in range(N):
    a, b = map(int, input().split())
    sums.append(a + b)
    diffs.append(a - b)

sums.sort(); diffs.sort()

print(max(sums[-1] - sums[0], diffs[-1] - diffs[0]))