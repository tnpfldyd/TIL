import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
meats = [tuple(map(int, input().split())) for _ in range(N)]
meats.sort(key=lambda x : (x[1], -x[0]))

total = meats[0][0]
same = meats[0][1]
answer = same if total >= M else INF

for i in range(1, N):
    weight, cost = meats[i]
    total += weight
    if cost == meats[i - 1][1]:
        same += cost
    else:
        same = cost
    if total >= M:
        answer = min(answer, same)
        if same == cost:
            break

print(answer if answer != INF else -1)