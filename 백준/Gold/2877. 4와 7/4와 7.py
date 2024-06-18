N = int(input())
result =''
while N > 0:
    t = N % 2
    N = N // 2
    if t:
        result = '4'+ result
    else:
        N -= 1
        result = '7'+ result
print(result)