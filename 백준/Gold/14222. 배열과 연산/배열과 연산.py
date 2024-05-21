N, K = map(int, input().split())
arr = sorted(map(int, input().split()), reverse=True)

visited = [False] * (N + 1)

for value in arr:
    s = 0
    while True:
        temp = value + s * K
        if temp > N:
            print(0)
            exit(0)
        if not visited[temp]:
            visited[temp] = True
            break
        s += 1

print(1)