import sys
sys.stdin = open('3456input.txt','r')

T = int(input())
for i in range(1, T+1):
    case_ = list(map(int, input().split()))
    sum_ = (min(case_) + max(case_)) * 2
    x = sum_ - sum(case_)
    print(f'#{i}', x)