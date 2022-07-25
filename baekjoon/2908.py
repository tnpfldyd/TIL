a, b = input().split()
A = int(a[::-1])
B = int(b[::-1])
if A > B :
    print(A)
else:
    print(B)