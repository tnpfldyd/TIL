import sys
from itertools import combinations

INF = sys.maxsize

n = int(input())
mp, mf, ms, mv = map(int, input().split())
nutrients = [list(map(int, input().split())) for _ in range(n)]

min_cost = INF
min_combi = []

for r in range(1, n+1):
    for combi in combinations(range(n), r):
        p, f, s, v, c = map(sum, zip(*[nutrients[idx] for idx in combi]))

        if p >= mp and f >= mf and s >= ms and v >= mv:
            if c < min_cost:
                min_cost = c
                min_combi = combi
            elif c == min_cost:
                    min_combi = sorted((min_combi, combi))[0]

if min_cost == INF:
    print(-1)
else:
    print(min_cost)
    print(' '.join([str(i+1) for i in min_combi]))