N, K = map(int, input().split())
people = [0] + list(map(int, input().split()))
visited = [False] * (N + 1)

cnt = p = 0
while p < N:
    n = i = 0
    for j in range(1, N + 1):
        if visited[j]:
            continue
        if n < people[j] and i < j:
            visited[j] = True
            p += 1
            n, i = people[j], j
    cnt += 1
print("NO" if cnt > K else "YES")