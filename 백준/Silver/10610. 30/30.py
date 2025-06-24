import sys
input = sys.stdin.readline

s = input().strip()
digits = list(s)

if '0' not in digits or sum(map(int, digits)) % 3 != 0:
    print(-1)
else:
    digits.sort(reverse=True)
    print(''.join(digits))