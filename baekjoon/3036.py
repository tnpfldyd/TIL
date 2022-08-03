def GCD(a, b):
    while b:
        a, b = b, a % b
    return a
T = int(input())
result = list(map(int, input().split()))
A = result[0]
result2 = result[1:]
for i in result2:
    X = GCD(A, i)
    print(f'{A//X}/{i//X}' )