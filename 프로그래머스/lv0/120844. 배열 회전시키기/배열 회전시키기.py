from collections import deque

def solution(numbers, direction):
    numbers = deque(numbers)
    if direction == 'right':
        numbers.appendleft(numbers.pop())
    else:
        numbers.append(numbers.popleft())
    return list(numbers)