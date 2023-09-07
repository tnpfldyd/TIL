N, M = map(int, input().split())
machines = list(map(int, input().split()))

if N < M:
    print(N)
else:
    s, e = 0, 2000000000 * 30
    t = 0
    while s <= e:
        mid = (s + e) // 2
        temp = M
        for i in range(M):
            temp += mid // machines[i]
        if temp < N:
            s = mid + 1
        else:
            t = mid
            e = mid - 1
    cnt = M
    for i in range(M):
        cnt += (t - 1) // machines[i]
    for i in range(M):
        if not t % machines[i]:
            cnt += 1
        if cnt == N:
            print(i + 1)
            break