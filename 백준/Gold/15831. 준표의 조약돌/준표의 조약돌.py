import sys
input = sys.stdin.readline

N, B, W = map(int, input().split())
load = input().rstrip()
left = 0
w_cnt = 0
b_cnt = 0
max_len = 0
for right in range(N):
    if load[right] == 'W':
        w_cnt += 1
    else:
        b_cnt += 1
    while b_cnt > B:
        if load[left] == 'W':
            w_cnt -= 1
        else:
            b_cnt -= 1
        left += 1
    if w_cnt >= W and b_cnt <= B:
        max_len = max(max_len, right - left + 1)
print(max_len)