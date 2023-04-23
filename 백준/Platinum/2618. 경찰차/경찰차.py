import sys
input = sys.stdin.readline
INF = sys.maxsize

N, W = int(input()), int(input())

dp = [[INF] * (W) for _ in range(W)]

pq = []

lo = [[], []]
lo[0].append((1, 1))
lo[1].append((N, N))

for _ in range(W):
    x, y = map(int, input().split())
    lo[0].append((x, y))
    lo[1].append((x, y))

def getDist(start, end, c):
    dist = abs(lo[c][start][0] - lo[c][end][0]) + abs(lo[c][start][1] - lo[c][end][1])
    return dist

def solve(a, b):

    if a == W or b == W:

        return 0
    ret = dp[a][b]
    if ret != INF:
        return ret
    event = max(a, b) + 1
    dist_a, dist_b = getDist(a, event, 0), getDist(b, event, 1)
    ret = min(solve(event, b) + dist_a, solve(a, event) + dist_b)

    dp[a][b] = ret
    return ret

def find_path(a, b):
    if a == W or b == W:
        return
    event = max(a, b) + 1
    dist_a, dist_b = getDist(a, event, 0), getDist(b, event, 1)
    res_a, res_b = solve(event, b) + dist_a, solve(a, event) + dist_b
    if res_a > res_b:
        print(2)
        find_path(a, event)
    else:
        print(1)
        find_path(event, b)
print(solve(0, 0))
find_path(0, 0)
