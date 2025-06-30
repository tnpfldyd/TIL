import sys
import math

a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())

numerator = a * d + c * b
denominator = b * d

gcd = math.gcd(numerator, denominator)
numerator //= gcd
denominator //= gcd

print(numerator, denominator)