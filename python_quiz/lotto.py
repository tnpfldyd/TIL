import random
n = int(input('구매할 갯수를 입력하세요. '))

for i in range(n):
    number = random.sample(range(1, 46), 6)
    number.sort()
    print(number)