import sys
input = sys.stdin.readline
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    elif a / b < 1:
        if b / a == b // a:
            print('factor')
        else:
            print('neither')
    elif a / b > 1:
        if a / b == a // b:
            print('multiple')
        else:
            print('neither')