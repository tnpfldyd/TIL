N, K = map(int, input().split())

if N == K:
    print("Impossible")
else:
    K = N - K
    s = 1
    if K % 2:
        print(1, end=" ")
        K -= 1
        s = 2
    i = s
    while i <= N:
        if K:
            print(i + 1, i, end=" ")
            K -= 2
            i += 1
        else:
            print(i, end=" ")
        i += 1