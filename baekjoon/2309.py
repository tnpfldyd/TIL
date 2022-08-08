result = [int(input()) for _ in range(9)]
result_sum = sum(result)
Target = 100
for i in range(len(result)-1):
    if len(result) < 9:
        break
    for j in range(i+1, len(result)):
        if Target == result_sum - (result[i] + result[j]):
            X = result[i]
            Y = result[j]
            result.remove(X)
            result.remove(Y)
            break
    
result.sort()
for i in result:
    print(i)