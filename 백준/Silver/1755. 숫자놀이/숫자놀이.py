import sys
input = sys.stdin.readline

M, N = map(int, input().split())

words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

numbers = []
for num in range(M, N + 1):
    if num < 10:
        english = words[num]
    else:
        tens = num // 10
        ones = num % 10
        english = words[tens] + " " + words[ones]
    numbers.append((english, num))

numbers.sort()

for i in range(len(numbers)):
    print(numbers[i][1], end='')
    if (i + 1) % 10 == 0:
        print()
    else:
        print(' ', end='')