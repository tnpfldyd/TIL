import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    x, y = map(int, input().split())

    dist = y - x
    maximum = int(dist ** 0.5)
    if maximum == dist ** 0.5:
        print(maximum * 2 - 1)
    elif dist <= maximum ** 2 + maximum:
        print(maximum * 2)
    else:
        print(maximum * 2 + 1)