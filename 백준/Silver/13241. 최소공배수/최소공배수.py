import math

a, b = map(int, input().split())
lcm = (a * b) // math.gcd(a, b)
print(lcm)