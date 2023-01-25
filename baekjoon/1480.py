import sys
input = sys.stdin.readline

N, M, C = map(int, input().split())
weight = list(map(int, input().strip().split()))
visited = [[[-1] * (1 << N) for _ in range(C + 1)] for _ in range(M + 1)]

def dfs(bag, total, bit):
    if bag == M:
        return -1
    if bit == (1 << N) - 1:
        return 0
    if visited[bag][total][bit] != -1:
        return visited[bag][total][bit]
    temp = 0
    for i in range(N):
        if not (bit & 1 << i) and weight[i] <= C:
            if weight[i] + total > C:
                temp = max(temp, dfs(bag + 1, weight[i], bit | 1 << i) + 1)
            else:
                temp = max(temp, dfs(bag, weight[i] + total, bit | 1 << i) + 1)
    visited[bag][total][bit] = temp
    return temp

print(dfs(0, 0, 0))