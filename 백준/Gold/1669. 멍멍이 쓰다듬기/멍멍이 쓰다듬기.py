import sys
a, b = map(int, input().split())
dif = b - a
day = 0
for i in range(1, 2 ** 31):
    for _ in range(2):
        if dif <= 0:
            print(day)
            sys.exit(0)
        day += 1
        dif -= i