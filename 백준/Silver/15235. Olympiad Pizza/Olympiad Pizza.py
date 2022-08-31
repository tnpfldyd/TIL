from collections import deque
import sys
input = sys.stdin.readline
T = int(input())
list_= list(map(int, input().rstrip().split()))
result = []
cnt = 0
start = deque()
for i in range(len(list_)):
    start.append((list_[i], i+1, 0))
while start:
    x, y, z = start.popleft()
    x -= 1
    cnt += 1
    if x == 0:
        result.append((x, y, cnt))
    else:
        start.append((x, y, cnt))
qwqw = sorted(result, key = lambda x : (x[1]))
for i in qwqw:
    print(i[2], end = ' ')