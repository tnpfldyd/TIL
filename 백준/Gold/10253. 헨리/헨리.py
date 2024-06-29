import sys, math
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    while a != 1:
        x = b // a + 1 if b % a else b // a
        a = a * x - b
        b *= x
        g = math.gcd(a, b)
        a //= g
        b //= g
    print(b)
