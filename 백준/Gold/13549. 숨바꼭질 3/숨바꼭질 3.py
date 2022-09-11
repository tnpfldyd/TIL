from collections import deque
import sys
input = sys.stdin.readline
N, K = map(int, input().rstrip().split())
list_ = [-1] * 100001
start = deque()
start.append(N)
list_[N] = 0
while start:
    x = start.popleft()
    if x == K:
        print(list_[x])
        break
    for i in (x*2, x-1, x+1):
        if i == x*2:
            if 0 <= i < 100001 and list_[i] == -1:
                list_[i] = list_[x]
                start.append(i)
        elif 0 <= i < 100001 and list_[i] == -1:
            list_[i] = list_[x] + 1
            start.append(i)