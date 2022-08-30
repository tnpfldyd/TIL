from collections import deque
import sys
input = sys.stdin.readline
N, K = map(int, input().rstrip().split())
list_ = [[-1, 0] for _ in range(100001)]
start = deque()
start.append(N)
list_[N][0] = 0
list_[N][1] = 1
while start:
    x = start.popleft()
    if x == K:
        print(list_[x][0])
        print(list_[x][1])
        break
    for i in (x-1, x+1, x*2):
        if 0 <= i < 100001:
            if list_[i][0] == -1:
                list_[i][0] = list_[x][0] + 1
                list_[i][1] = list_[x][1]
                start.append(i)
            elif list_[i][0] == list_[x][0] + 1:
                list_[i][1] += list_[x][1]