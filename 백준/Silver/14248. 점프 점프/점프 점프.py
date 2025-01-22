from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
stones = list(map(int, input().split()))
S = int(input()) - 1
visited = [False] * N
visited[S] = True
q = deque([S])

while q:
    x = q.popleft()
    temp = [stones[x], -stones[x]]
    for t in temp:
        nx = x + t
        if 0 <= nx < N and not visited[nx]:
            visited[nx] = True
            q.append(nx)

print(sum(visited))