gcd, lcm = map(int, input().split())
result_a, result_b = 0, 0

def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n = lcm // gcd

for i in range(1, int(n ** 0.5) + 1):
    if not n % i:
        a, b = i, n // i

        if get_gcd(a, b) == 1:
            result_a, result_b = a, b

print(result_a * gcd, result_b * gcd)