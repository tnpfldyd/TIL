import itertools
number = [-3, -2, -1, 0, 1, 2, 3]
result = 0
for i in itertools.combinations(number, 3):
    if sum(i) == 0:
        result += 1
print(result)