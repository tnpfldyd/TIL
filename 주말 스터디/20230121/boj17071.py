from collections import deque
visited = [[False] * 500001 for _ in range(2)]
N, K = map(int, input().split())
visited[0][N] = True
start = deque()
start.append(N)
time = 0
if N == K:
    print(0)
else:
    while start:
        temp = deque()
        time += 1
        K += time
        if K > 500000:
            print(-1)
            break
        for i in range(len(start)):
            x = start.popleft()
            for j in (x-1, x+1, x*2):
                if 0 <= j <= 500000 and not visited[time%2][j]:
                    visited[time%2][j] = True
                    temp.append(j)
        if visited[time%2][K]:
            print(time)
            break
        start = temp
    else:
        print(-1)