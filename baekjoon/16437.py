import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = int(input())
matrix = [[] for _ in range(N + 1)]
island = [0] * (N + 1)

for i in range(2, N + 1):
    t, a, p = input().split()
    a, p = map(int, (a, p))
    matrix[p].append(i)
    island[i] = a if t == 'S' else -a

def dfs(cur):
    if not matrix[cur]:
        return island[cur] if island[cur] > 0 else 0
    let = island[cur]
    for nxt in matrix[cur]:
        let += dfs(nxt)
    return let if let > 0 else 0

print(dfs(1))
