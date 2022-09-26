numbers = [3, 30, 34, 5, 9,300]
number = []
for i in numbers:
    number.append(str(i))
number.sort(key = lambda x : x*100, reverse=True)
print(number)