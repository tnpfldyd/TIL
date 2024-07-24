import sys
import math
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    m = int(input())
    if m == 1:
        print(1)
    else:
        r = sum(math.log10(i) for i in range(1, m + 1))
        print(int(math.ceil(r)))
