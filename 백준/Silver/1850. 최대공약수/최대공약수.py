import math

a, b = map(int, input().split())

gcd_length = math.gcd(a, b)
result = '1' * gcd_length

print(result)