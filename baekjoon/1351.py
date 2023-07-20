from collections import defaultdict
N, P, Q = map(int, input().split())

numbers = defaultdict(int)
numbers[0] = 1

def dfs(x):
    if numbers[x]:
        return numbers[x]
    numbers[x] = dfs(x // P) + dfs(x // Q)
    return numbers[x]
print(dfs(N))