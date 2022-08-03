
def GCD(a, b):
    while b:
        a, b = b, a % b
    return a

def LCM(a, b):
    result = (a * b) // GCD(a, b)
    return result
T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    print(LCM(a, b))