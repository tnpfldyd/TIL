T = int(input())

for i in range(1, T+1):
    Q = int(input())
    cnt = [0] * 5
    while Q:
        if Q % 2 == 0:
            Q /= 2
            cnt[0] += 1
        elif Q % 3 == 0:
            Q /= 3
            cnt[1] += 1
        elif Q % 5 == 0:
            Q /= 5
            cnt[2] += 1
        elif Q % 7 == 0:
            Q /= 7
            cnt[3] += 1
        elif Q % 11 == 0:
            Q /= 11
            cnt[4] += 1
        elif Q == 1:
            break
    print('#'+str(i), *cnt)
