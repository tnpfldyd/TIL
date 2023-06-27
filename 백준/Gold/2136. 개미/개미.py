import sys
input = sys.stdin.readline
N, L = map(int, input().split())
Ants = [int(input().strip()) for _ in range(N)]
La = Ra = 0
cnt = 0
ant_info = []
for idx, cost in enumerate(Ants, 1):
    if cost > 0:
        Ra = max(Ra, L - cost)
    else:
        cnt += 1
        La = max(La, abs(cost))
    ant_info.append((abs(cost), idx))

ant_info.sort()
if La < Ra:
    print(ant_info[cnt][1], Ra)
else:
    print(ant_info[cnt - 1][1], La)