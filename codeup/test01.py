numbers = [0, 20, 100]
result = numbers[0]

for i in numbers:
    if i > result:
        result = i
print(result)