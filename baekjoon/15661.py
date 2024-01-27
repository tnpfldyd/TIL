import sys
input = sys.stdin.readline
INF = sys.maxsize

def cal(team):
    result = 0
    for i in team:
        for j in team:
            result += power[i][j]
    return result

def splitTeam(num):
    start, link = [], []
    for i in range(N):
        if (num & (1 << i)):
            link.append(i)
        else:
            start.append(i)
    return abs(cal(link) - cal(start))

N = int(input())
power = [list(map(int, input().split())) for _ in range(N)]

answer = INF

for i in range(1, (1 << N) - 1):
    answer = min(answer, splitTeam(i))

print(answer)