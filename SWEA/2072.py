import sys

sys.stdin = open("2072input.txt", "r")

T = int(input())


for i in range(1, T + 1):
    b = map(int, input().split())
    result = 0
    for j in b:
        if j%2 == 1:
            result += j
    print('#'+str(i),result)