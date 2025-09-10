import sys
import math
input = sys.stdin.readline

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def get_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sorted(divisors)

R, G = map(int, input().split())

g = gcd(R, G)
divisors = get_divisors(g)

for d in divisors:
    N = d
    X = R // d
    Y = G // d
    print(N, X, Y)