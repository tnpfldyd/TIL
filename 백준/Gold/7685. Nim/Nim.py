import sys
input = sys.stdin.readline

while 1:
    N = int(input())
    if not N:
        break
    P = tuple(map(int, input().split()))
    bit = res = 0
    for p in P:
        bit ^= p
    for p in P:
        temp = bit ^ p
        if temp < p:
            res += 1
    print(res)