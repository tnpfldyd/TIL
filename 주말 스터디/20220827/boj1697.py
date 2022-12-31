from collections import deque
import sys
input = sys.stdin.readline
N, K = map(int, input().rstrip().split())
list_ = [0] * 100001
start = deque()
start.append(N)

while start:
    x = start.popleft()
    if x == K:
        print(list_[x])
        break
    for i in (x-1, x+1, x*2):
        if 0 <= i < 100001 and list_[i] == 0:
            list_[i] = list_[x] + 1
            start.append(i)