
N = int(input())
n1 = 0
n2 = 1
result = 1
if N > 2:
    for i in range(2, N+1):
        result = n1 + n2
        n1 = n2
        n2 = result
print(result)