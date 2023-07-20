N = int(input())
numbers = list(map(int, input().split()))
visited = [False] * 100001
r = answer = 0
for l in range(N):
    while r < N:
        if visited[numbers[r]]:
            break
        visited[numbers[r]] = True
        r += 1
    answer += (r - l)
    visited[numbers[l]] = False
print(answer)