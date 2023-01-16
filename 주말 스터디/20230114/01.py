import sys
input = sys.stdin.readline
N = int(input())
num_list = list(map(int, input().strip().split()))
one_cnt = 0
two_cnt = 0
max_cnt = 0
for i in num_list:
    if i == 1:
        one_cnt += 1
        two_cnt -= 1
    else:
        one_cnt -= 1
        two_cnt += 1
    one_cnt = max(one_cnt, 0)
    two_cnt = max(two_cnt, 0)
    max_cnt = max(max_cnt, one_cnt, two_cnt)
print(max_cnt)

