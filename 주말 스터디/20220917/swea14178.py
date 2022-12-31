import math
T = int(input())
for i in range(1, T+1):
    a, b = map(int, input().split())
    cnt = math.ceil(a / ((b*2) + 1))
    print(f'#{i} {cnt}')