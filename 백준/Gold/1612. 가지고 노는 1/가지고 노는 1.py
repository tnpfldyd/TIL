import sys
input = sys.stdin.readline
N = int(input())
if N == 1:
    print(1)
elif not N % 2 or not N % 5:
    print(-1)
else:
    x = 1
    time = 1
    while x != 0:
        x += (9 * x + 1) % N
        x = x % N
        time += 1
    print(time)