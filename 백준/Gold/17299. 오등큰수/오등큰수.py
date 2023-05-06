N = int(input())
numbers = list(map(int, input().split()))
F = [0] * 1000001
for number in numbers:
    F[number] += 1
stack = []
answer = [0] * N

for i in range(N-1, -1, -1):
    height = F[numbers[i]]
    while stack and height >= F[numbers[stack[-1]]]:
        stack.pop()
    answer[i] = -1
    if stack:
        answer[i] = numbers[stack[-1]]
    stack.append(i)

print(*answer)