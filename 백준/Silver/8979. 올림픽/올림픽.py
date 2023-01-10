import sys
input = sys.stdin.readline
N, target = map(int, input().split())
ranking = []
for i in range(N):
    num, g, s, b = map(int, input().split())
    ranking.append((g, s, b, num))
ranking.sort(reverse=True)
cnt, tied = 0, 0
tg, ts, tb = 0, 0, 0
for g, s, b, num in ranking:
    if (g, s, b) == (tg, ts, tb):
        tied += 1
    else:
        cnt += 1 + tied
        tied = 0
        tg, ts, tb = g, s, b
    if num == target:
        print(cnt)
        break
