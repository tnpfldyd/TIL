import sys

sys.stdin = open("1285input.txt", "r")
T = int(input())
for i in range(1, T):
    A = int(input())
    B = map(int, input().split())
    C = list(map(abs, B))
    D = min(C)
    cnt = 0
    for j in C:
        if j == D:
            cnt += 1
    print('#'+str(i), D, cnt)