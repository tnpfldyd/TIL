import bisect
N = int(input())
numbers = list(map(int, input().split()))
rev_numbers = reversed(numbers)
stack = []
rev_stack = []
answer = []
rev_answer = []
for number, rev_number in zip(numbers, rev_numbers):
    if not stack:
        stack.append(number)
    else:
        if stack[-1] < number:
            stack.append(number)
        else:
            idx = bisect.bisect_left(stack, number)
            stack[idx] = number
    if not rev_stack:
        rev_stack.append(rev_number)
    else:
        if rev_stack[-1] < rev_number:
            rev_stack.append(rev_number)
        else:
            idx = bisect.bisect_left(rev_stack, rev_number)
            rev_stack[idx] = rev_number
    answer.append(len(stack)), rev_answer.append(len(rev_stack))
result = 0
for a, b in zip(answer, reversed(rev_answer)):
    temp = a + b - 1
    if result < temp:
        result = temp
print(result)