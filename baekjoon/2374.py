import sys
input = sys.stdin.readline

N = int(input())
count = 0
current_number = int(input())
max_number = current_number
for _ in range(N - 1):
    next_number = int(input())
    if current_number < next_number:
        count += next_number - current_number
        max_number = max(max_number, next_number)
    current_number = next_number
count += max_number - current_number
print(count)