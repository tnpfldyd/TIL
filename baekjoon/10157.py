from pprint import pprint
x, y = map(int, input().split())
target = int(input())
visit = [[0] * x for _ in range(y)]
dx, dy = [0, 1, 0, -1],[1, 0, -1, 0] # 하 우 상 좌
start = [(0, 0)]
visit[0][0] = 1
s, f = 1, 0
if x * y < target:
    print(0)
    exit()
while start:
    a, b = start.pop()
    if s == target:
        print(b+1, a+1)
        break
    if 0 <= a + dy[f] < y and 0 <= b + dx[f] < x and visit[a + dy[f]][b + dx[f]] == 0:
        s += 1
        a += dy[f]; b += dx[f]
        visit[a][b] = s
        start.append((a, b))
    else:
        f = (f + 1) % 4
        start.append((a, b))
pprint(visit)