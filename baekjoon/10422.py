from math import factorial
T = int(input())
for i in range(T):
    a = int(input())
    cnt = 0
    if a % 2 == 1:
        print(cnt)
        continue
    # 1 2 5 14 42 132 429 1430 4862 16796
    else:
        a //= 2
    cnt = (factorial(2*a) // (factorial(a) * factorial(a+1))) % 1000000007
    print(cnt)