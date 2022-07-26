a, b = map(int, input().split())

def GCD(a, b):
    while b:
        a, b = b, a % b
    return a
print(GCD(a, b))
def LCM(a, b):
    result = (a * b) // GCD(a, b)
    return result
print(LCM(a, b))
