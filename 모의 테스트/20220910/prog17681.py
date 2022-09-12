n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
for i in range(n):
    arr1[i] = format(arr1[i], 'b')
    arr2[i] = format(arr2[i], 'b')
for i in range(n):
    if len(arr1[i]) != n:
        arr1[i] = ('0' * (n - len(arr1[i]))) + arr1[i]
    if len(arr2[i]) != n:
        arr2[i] = ('0' * (n - len(arr2[i]))) + arr2[i]
result = []
for i in range(n):
    answer = []
    for j in range(n):
        if arr1[i][j] == '1' or arr2[i][j] == '1':
            answer.append('#')
        else:
            answer.append(' ')
    result.append(''.join(answer))
print(result)