import sys

sys.stdin = open("2068input.txt", "r")

T = int(input())

for i in range(1, T + 1):
    b = list(map(int, input().split()))
    print('#' + str(i), sorted(b)[-1])
