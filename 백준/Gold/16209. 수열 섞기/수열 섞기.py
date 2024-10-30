N = int(input().strip())
numbers = list(map(int, input().strip().split()))
numbers.sort()

negative_index = 0
while negative_index < N and numbers[negative_index] < 0:
    negative_index += 1

negative_numbers = numbers[0:negative_index:2][::-1] + numbers[1:negative_index:2]

positive_index = N - 1
while positive_index >= 0 and numbers[positive_index] > 0:
    positive_index -= 1

positive_numbers = numbers[positive_index + 1:N:2] + numbers[positive_index + 2:N:2][::-1]

zero_list = [0] * (positive_index - negative_index + 1)

if negative_numbers and negative_numbers[0] > negative_numbers[-1]:
    negative_numbers.reverse()
if positive_numbers and positive_numbers[0] > positive_numbers[-1]:
    positive_numbers.reverse()

print(*(negative_numbers + zero_list + positive_numbers))
