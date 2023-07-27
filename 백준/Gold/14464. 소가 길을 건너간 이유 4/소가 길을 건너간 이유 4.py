import sys

input = sys.stdin.readline
C, N = map(int, input().split())
chickens = sorted([int(input()) for _ in range(C)])
cows = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x : x[1])
answer = 0
visited = [False] * C

for s, e in cows:
    for idx, chicken in enumerate(chickens):
        if s <= chicken <= e and not visited[idx]:
            answer += 1
            visited[idx] = True
            break

print(answer)