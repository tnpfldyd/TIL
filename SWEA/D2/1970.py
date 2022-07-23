import sys

sys.stdin = open("1970input.txt", "r")

T = int(input())
for i in range(1, T+1):
    W = int(input())
    A = [5000, 1000, 500, 100, 50, 10, 5, 1]
    won = W // 10
    result = [0] * 8
    for j in range(len(A)):
        if won // A[j] > 0:
            result[j] = won // A[j]
            won = won%A[j]
    print('#'+str(i))
    print(*result)

