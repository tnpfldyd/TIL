from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

def main():
    def dfs(cur):
        visited[cur] = True
        
        dp[cur][0] = 0
        dp[cur][1] = person[cur]
        
        for nxt in graph[cur]:
            if visited[nxt]:
                continue
            dfs(nxt)
            dp[cur][0] += max(dp[nxt])
            dp[cur][1] += dp[nxt][0]
    N = int(input())
    person = [0] + list(map(int, input().split()))
    dp = [[0] * 2 for _ in range(N + 1)]
    visited = [False] * (N + 1)
    graph = defaultdict(list)
    for _ in range(N - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    dfs(1)
    print(max(dp[1]))

if __name__ == '__main__':
    main()
