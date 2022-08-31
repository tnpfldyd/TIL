from collections import deque
import sys
input = sys.stdin.readline
N, K = map(int, input().rstrip().split())
list_ = [-1] * 100001
start = deque()
start.append(N)
list_[N] = 0
cnt = 0
while start:
    x = start.popleft()
    if x == K:
        cnt += 1
    for i in (x-1, x+1, x*2):
        if 0 <= i < 100001:
            if list_[i] == -1 or list_[i] == list_[x] + 1:
                list_[i] = list_[x] + 1
                start.append(i)
print(list_[K])
print(cnt)