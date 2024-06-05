from collections import defaultdict
import sys
input = sys.stdin.readline

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
            
    def get_path(now, prev):
        if dp[now][1] > dp[now][0] and not visited[prev]:
            path.append(now)
            visited[now] = True
        
        for next_node in graph[now]:
            if next_node == prev:
                continue
            get_path(next_node, now)

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
    visited = [False] * (N + 1)
    path = []
    get_path(1, 0)
    path.sort()
    print(max(dp[1]))
    print(*path)

if __name__ == '__main__':
    main()
