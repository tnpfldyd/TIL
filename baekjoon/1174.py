import itertools

N = int(input())

numbers = []
for i in range(1, 11):
    for combination in itertools.combinations(range(10), i):
        combination = list(combination)
        combination.sort(reverse=True)
        numbers.append(int("".join(map(str, combination))))

numbers.sort()

try:
    print(numbers[N - 1])
except:
    print(-1)