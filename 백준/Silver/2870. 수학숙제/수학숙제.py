import re,sys
input = sys.stdin.readline

n = int(input())
numbers = []

for _ in range(n):
    line = input()
    found_numbers = re.findall(r'\d+', line)
    for num_str in found_numbers:
        numbers.append(int(num_str))

numbers.sort()

for num in numbers:
    print(num)