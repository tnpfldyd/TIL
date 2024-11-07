import sys
from collections import defaultdict

INF = 20001
graph = defaultdict(list)
dp = [0] * 1001

def f(node, parent):
    if dp[node] == 0:
        res = INF
        total_sum = 0

        for child, child_weight in graph[node]:
            if child == parent:
                res = child_weight
                continue

            if len(graph[child]) == 1:
                total_sum += child_weight
            else:
                total_sum += f(child, node)

        res = min(res, total_sum)
        dp[node] = res

    return dp[node]

def main():
    input = sys.stdin.readline

    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())

        for i in range(1, N + 1):
            graph[i].clear()
            dp[i] = 0

        for _ in range(M):
            a, b, c = map(int, input().split())
            graph[a].append((b, c))
            graph[b].append((a, c))

        print(f(1, 0))

if __name__ == "__main__":
    main()