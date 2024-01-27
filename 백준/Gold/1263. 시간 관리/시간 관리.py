import sys
input = sys.stdin.readline

N = int(input())
schedules = []
for _ in range(N):
    t, s = map(int, input().split())
    schedules.append((s, t))
schedules.sort(reverse=True)

answer = schedules[0][0] - schedules[0][1]

for i in range(1, N):
    if answer > schedules[i][0]:
        answer = schedules[i][0] - schedules[i][1]
    else:
        answer -= schedules[i][1]
    if answer < 0:
        print(-1)
        break
else:
    print(answer)