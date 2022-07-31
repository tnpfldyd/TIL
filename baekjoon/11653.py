T = int(input())
cnt = 2
while T > 1:
    if T % cnt == 0:
        T //= cnt
        print(cnt)
    else:
        cnt += 1
        if T % cnt == 0:
            T //= cnt
            print(cnt)
