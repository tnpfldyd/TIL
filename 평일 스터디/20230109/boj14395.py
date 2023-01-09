from collections import deque
start1, end = map(int, input().split())
visited = set()
start = deque()
start.append((start1, ''))
visited.add(start1)
if start1 == end:
    print(0)
elif end == 0:
    print('-')
else:
    while start:
        x, clip = start.popleft()
        if x == end:
            print(clip)
            break
        if 0 <= x*x < 1000000001 and x*x not in visited:
            visited.add(x*x)
            start.append((x*x, clip+'*'))
        if 0 <= x+x < 1000000001 and x+x not in visited:
            visited.add(x+x)
            start.append((x+x, clip+'+'))
        if x//x not in visited:
            visited.add(x//x)
            start.append((x//x, clip+'/'))
    else:
        print(-1)