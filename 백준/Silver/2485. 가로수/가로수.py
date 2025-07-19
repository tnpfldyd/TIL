import sys
from math import gcd
from functools import reduce

input = sys.stdin.readline
n = int(input())
pos = [int(input()) for _ in range(n)]
dist = [pos[i] - pos[i-1] for i in range(1, n)]
g = reduce(gcd, dist)
print(sum(d // g - 1 for d in dist))