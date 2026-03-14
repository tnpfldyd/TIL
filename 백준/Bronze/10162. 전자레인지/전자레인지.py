T = int(input())

if T % 10 != 0:
    print(-1)
else:
    A = T // 300
    T %= 300

    B = T // 60
    T %= 60

    C = T // 10

    print(A, B, C)