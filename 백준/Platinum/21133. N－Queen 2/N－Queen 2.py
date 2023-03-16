
# https://en.wikipedia.org/wiki/Eight_queens_puzzle#Explicit_solutions

N = int(input())
isOdd = False

if N % 2:
    isOdd = True

if (not isOdd and N % 6 != 2) or (isOdd and (N - 1) % 6 != 2):
    if isOdd:
        N -= 1
    for i in range(1, N // 2 + 1):
        print(2 * i)
    for i in range(1, N // 2 + 1):
        print(2 * i - 1)
    if isOdd:
        print(N + 1)

elif (not isOdd and N // 6) or (isOdd and (N - 1) // 6 != 2):
    if isOdd:
        N -= 1
    for i in range(1, N // 2 + 1):
        print(1 + (2 * i + N // 2 - 3) % N)
    for i in range(N // 2, 0, -1):
        print(N - (2 * i + N // 2 - 3) % N)
    if isOdd:
        print(N + 1)
