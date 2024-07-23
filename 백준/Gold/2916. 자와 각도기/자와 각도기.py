from collections import deque

N, K = map(int, input().split())
deg = list(map(int, input().split()))
res = list(map(int, input().split()))
possible = [0] * 360
possible[0] = 1
q = deque([0])

while q:
    curr_deg = q.popleft()
    for d in deg:
        small = (d - curr_deg) % 360
        big = (d + curr_deg) % 360

        if not possible[small]:
            possible[small] = 1
            q.append(small)
        if not possible[big]:
            possible[big] = 1
            q.append(big)

for angle in res:
    if possible[angle]:
        print('YES')
    else:
        print('NO')
