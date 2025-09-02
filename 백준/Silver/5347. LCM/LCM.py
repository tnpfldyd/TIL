import sys, math
input = sys.stdin.readline

def lcm(x, y):
    return (x * y) // math.gcd(x, y)

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(lcm(a, b))