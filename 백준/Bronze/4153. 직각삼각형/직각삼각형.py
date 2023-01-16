import sys
input = sys.stdin.readline
while True:
    numbers = list(map(int, input().strip().split()))
    if numbers.count(0) == 3:
        break
    numbers.sort()
    a, b, c = numbers
    print('right' if a**2 + b**2 == c**2 else 'wrong')