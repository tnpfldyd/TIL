N = int(input())
num = list(map(int, input().split()))

if N == 1:
    print("A")
elif N == 2:
    if num[0] == num[1]:
        print(num[1])
    else:
        print("A")
else:
    a = 0
    if num[1] - num[0]:
        a = (num[2] - num[1]) // (num[1] - num[0])

    b = num[1] - num[0] * a

    for i in range(1, N):
        if num[i] != num[i - 1] * a + b:
            print("B")
            break
    else:
        print(num[N - 1] * a + b)