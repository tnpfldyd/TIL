import math
import sys
from functools import reduce

sys.setrecursionlimit(10 ** 6)

def find_cycle_length(x, start):
    visited[x] = True
    if sequence[x] == start:
        return 1
    elif not visited[sequence[x]]:
        return 1 + find_cycle_length(sequence[x], start)
    return 0

n = int(input())
sequence = [None] + list(map(int, input().split()))
visited = [False] * (n + 1)
cycle_lengths = []

for i in range(1, n + 1):
    if not visited[i]:
        cycle_lengths.append(find_cycle_length(i, i))

lcm_of_cycles = reduce(math.lcm, cycle_lengths)
print(lcm_of_cycles)
