from collections import deque
import sys
input = sys.stdin.readline
arr = ''
for _ in range(3):
    temp = input().strip()
    arr += temp.replace(' ', '')
start = deque()
visited = set()
start.append((arr, 0))
visited.add(arr)
dx, dy = [0,0,-1,1], [1,-1,0,0]
while start:
    arr, cnt = start.popleft()
    if arr == '123456780':
        print(cnt)
        break
    temp = arr.find('0')
    x = temp // 3
    y = temp % 3
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < 3 and 0 <= ny < 3:
            ntemp = nx * 3 + ny
            na = list(arr)
            na[ntemp], na[temp] = na[temp], na[ntemp]
            na = ''.join(na)
            if na not in visited:
                visited.add(na)
                start.append((na, cnt+1))
else:
    print(-1)