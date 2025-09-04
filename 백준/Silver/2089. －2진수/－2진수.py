N = int(input())

if N == 0:
    print(0)
else:
    result = ""
    while N != 0:
        if N % (-2) == 0:
            result = "0" + result
            N //= -2
        else:
            result = "1" + result
            N = (N - 1) // (-2)
    print(result)