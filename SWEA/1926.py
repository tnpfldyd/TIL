T = int(input())

for i in range(1, T +1):
    j = str(i)
    result = 0
    
    for q in j:
        if q in '369':
            result += 1
    if result == 0:
        print(j, end=' ')
    else:
        print('-' * result, end=' ')
