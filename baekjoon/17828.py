N, X = map(int, input().split())

if 26 * N < X or X < N:
    print("!")
else:
    result = ['A'] * N

    X -= N

    for i in range(N - 1, -1, -1):
        temp = min(X, 25)
        result[i] = chr(ord(result[i]) + temp)
        X -= temp

    print(''.join(result))