import math

s = input().strip()
t = input().strip()

lcm = len(s) * len(t) // math.gcd(len(s), len(t))

print(int(s * (lcm // len(s)) == t * (lcm // len(t))))
