import sys
input = sys.stdin.readline

N = int(input())
maxNum = 0
sums = 0
for _ in range(N):
    x = int(input())
    maxNum = max(maxNum, x)
    sums += x

sums -= maxNum
print((sums + maxNum) % 2 if sums > maxNum else maxNum - sums)