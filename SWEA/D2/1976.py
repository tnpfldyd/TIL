import sys

sys.stdin = open("1976input.txt", "r")

T = int(input())

for i in range(1, T+1):
    a, b, c, d = list(map(int, input().split()))
    time = 0
    minit = 0
    if a + c > 12:
        time = a + c - 12
    else:
        time = a + c
    if b + d >= 60:
        time += 1
        minit = b + d - 60
    else:
        minit = b + d
    if time > 12:
        time -= 12
    print('#'+str(i), time, minit)