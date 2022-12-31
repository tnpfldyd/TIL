import sys
INF = sys.maxsize
T = 10
for i in range(1, T+1):
    result = 0
    N = int(input())
    list_ = list(map(int, input().split()))
    for j in range(2, N-2):
        temp = INF
        for k in range(-2, 3):
            if k == 0:
                continue
            temp = min(temp, list_[j]-list_[j-k])
        if temp > 0:
            result += temp
    print(f'#{i} {result}')