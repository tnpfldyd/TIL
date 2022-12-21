number = 10
limit = 3
power = 2
result = 0
temp = [0] * (number+1)
for i in range(1, number+1):
    for j in range(i, number+1, i):
        temp[j] += 1
for i in range(1, number+1):
    if temp[i] > limit:
        result += power
    else:
        result += temp[i]
print(temp)