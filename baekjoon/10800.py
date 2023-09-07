from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
balls = []
for i in range(N):
    c, w = map(int, input().split())
    balls.append((w, c, i))
balls.sort()

sums = 0
colors = defaultdict(int)
weights = defaultdict(int)
result = [0] * N
for i in range(N):
    w, c, idx = balls[i]
    colors[c] += w
    weights[w] += w
    sums += w
    result[idx] = sums - colors[c] - weights[w] + w
    if i and (balls[i - 1][1] == c and balls[i - 1][0] == w):
        result[idx] = result[balls[i - 1][2]]
        
for res in result:
    print(res)