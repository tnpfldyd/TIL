A, B, C = map(int, input().split())

def power(a, b, c):
    if b == 1:
        return a % c
    temp = power(a, b // 2, c)
    if b % 2 == 0:
        return (temp * temp) % c
    else:
        return (temp * temp * a) % c

print(power(A, B, C))