import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x, y = find(x), find(y)

    if x > y:
        x, y = y, x
    parent[y] = x

N, M, K = map(int, input().split())
candies = [0] + list(map(int, input().split()))
parent = list(range(N + 1))
group_size = [1] * (N + 1)

for _ in range(M):
    kid_a, kid_b = map(int, input().split())
    union(kid_a, kid_b)

total_candies = candies[:]
for kid in range(1, N + 1):
    if kid != parent[kid]:
        root = find(kid)
        total_candies[root] += total_candies[kid]
        group_size[root] += group_size[kid]

dp = [0] * K

for i in range(1, N + 1):
    if i != parent[i]:
        continue
    for j in range(K - 1, group_size[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - group_size[i]] + total_candies[i])

print(max(dp))
