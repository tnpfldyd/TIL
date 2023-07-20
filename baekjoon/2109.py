import sys
input = sys.stdin.readline
N = int(input())
max_day = 0
pays = []
for _ in range(N):
    pay = tuple(map(int, input().split()))
    max_day = max(max_day, pay[1])
    pays.append(pay)

pays = sorted(pays, key=lambda x : -x[0])
visited = [False] * (max_day + 1)
answer = 0
for i in range(N):
    for j in range(pays[i][1], 0, -1):
        if not visited[j]:
            answer += pays[i][0]
            visited[j] = True
            break

print(answer)