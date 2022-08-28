from collections import deque
result = [0] * 100001
a, b, start, end = map(int, input().split())
stat = deque()
stat.append(start)
while stat:
    x = stat.popleft()
    if x == end:
        print(result[x])
        break
    for i in (x+1, x-1, x+a, x-a, x+b, x-b, x*a, x*b):
        if 0 <= i <= 100000 and result[i] == 0:
            result[i] = result[x] + 1
            stat.append(i)
