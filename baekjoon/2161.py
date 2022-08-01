from collections import deque
numbers = deque(range(1, int(input())+1))
while len(numbers) > 1:
    print(numbers.popleft())
    numbers.append(numbers.popleft())
print(numbers[0])