num_list = [100, 95, 2, 4, 5, 6, 18, 33, 948]
n = 3
result = []
temp = []
for idx, num in enumerate(num_list, 1):
    temp.append(num)
    if not idx % n:
        result.append(temp)
        temp = []
print(result)