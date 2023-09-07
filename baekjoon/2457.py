from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
q = []
for _ in range(N):
    sm, sd, em, ed = map(int, input().split())
    q.append((sm * 100 + sd, em * 100 + ed))

q = deque(sorted(q))
day = 301
cnt = 0
while q:
    if day >= 1201 or q[0][0] > day:
        break
    temp = 0
    for _ in range(len(q)):
        if q[0][0] <= day:
            s, e = q.popleft()
            temp = max(temp, e)
        else:
            break
    day = temp
    cnt += 1

print(cnt if day >= 1201 else 0)