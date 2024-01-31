import sys
input = sys.stdin.readline

N = int(input())
numbers = sorted([int(input()) for _ in range(N)])
answer = 0

for i in range(N - 2):
    a = abs(-numbers[0] + numbers[i + 1] * 2 - numbers[i + 2])
    c = abs(numbers[i] - numbers[i + 1] * 2 + numbers[N - 1])
    answer = max(answer, a, c)

print(answer)