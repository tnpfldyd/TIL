import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    x_to_ys = {}

    for _ in range(N):
        x, y = map(int, input().split())
        if x not in x_to_ys:
            x_to_ys[x] = []
        x_to_ys[x].append(y)

    sorted_keys = sorted(x_to_ys.items())
    path = [[0, 0]]

    for x, ys in sorted_keys:
        ys.sort()
        if path[-1][1] != ys[0]:
            ys.sort(reverse=True)
        for y in ys:
            path.append([x, y])

    query = list(map(int, input().split()))
    for idx in query[1:]:
        print(*path[idx])