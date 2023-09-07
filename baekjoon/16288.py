N, K = map(int, input().split())
people = list(map(int, input().split()))
visited = [False] * N

cnt = p = 0
while p < N:
    prev = 0
    for i in range(N):
        if visited[i]:
            continue
        cur = people[i]
        if prev < cur:
            visited[i] = True
            p += 1
            prev = cur
    cnt += 1
print("NO" if cnt > K else "YES")