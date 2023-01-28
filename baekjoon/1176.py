import sys
input = sys.stdin.readline
N, K = map(int, input().split())
person = [0] * N
for i in range(N):
    person[i] = int(input())
answer = 0
def dfs(node, bit):
    if bit == (1 << N) - 1:
        return 1
    if visited[node][bit] != -1:
        return visited[node][bit]
    ret = 0
    for i in range(N):
        if not bit & (1 << i) and abs(person[node] - person[i]) > K:
            ret += dfs(i, bit | 1 << i)
    visited[node][bit] = ret
    return ret
for i in range(N):
    visited = [[-1] * (1 << N) for _ in range(N)]
    answer += dfs(i, 1 << i)
print(answer)