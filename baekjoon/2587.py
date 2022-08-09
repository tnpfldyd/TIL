result = []
for i in range(5):
    num = int(input())
    result.append(num)
result.sort()
print(sum(result)//5)
print(result[2])