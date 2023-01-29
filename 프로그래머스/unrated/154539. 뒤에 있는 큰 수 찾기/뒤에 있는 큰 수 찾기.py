def solution(numbers):
    answer = [0] * len(numbers)
    stack = []
    for i in range(len(numbers)):
        if not stack or numbers[i-1] > numbers[i]:
            stack.append(i)
        else:
            while stack and numbers[stack[-1]] < numbers[i]:
                answer[stack.pop()] = numbers[i]
            stack.append(i)
    while stack:
        answer[stack.pop()] = -1
    return answer