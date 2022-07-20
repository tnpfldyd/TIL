import sys

sys.stdin = open("1859input.txt", "r")

T = int(input())

for i in range(1, T+1):
    R = int(input())
    E = list(map(int, input().split()))
    last = E[-1]
    result = 0
    for j in range(R-2, -1, -1):
        if E[j] >= last:
            last = E[j]
        else:
            result += last - E[j]
    print('#'+str(i), result)