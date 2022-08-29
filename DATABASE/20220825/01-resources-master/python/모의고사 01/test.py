from collections import deque

numbers = [1, 2, 3, 4, 5]

queue = deque(numbers)

queue.append(6)

queue.popleft()

for num in queue:
    print(num, end=" ")

print(list(queue))