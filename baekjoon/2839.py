T = int(input())
cnt = 0
while T >= 0:
    if T % 5 == 0:
        cnt += T // 5
        print(cnt)
        break
    else:
        T -= 3
        cnt += 1
        if T == 0:
            print(cnt)
            break
if T < 3 and T != 0:
    print(-1)
