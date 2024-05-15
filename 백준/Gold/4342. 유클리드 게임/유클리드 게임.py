def func(a, b):
    if a > b:
        a, b = b, a
    if not b % a or b - a > a:
        return True
    return not func(a, b - a) 

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if func(a, b):
        print('A wins')
    else:
        print('B wins')