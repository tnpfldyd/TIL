import sys
input = sys.stdin.readline

N = int(input())
numbers = [(int(input()), i) for i in range(N)]
sortNumbers = sorted(numbers)
result = 0
for i in range(N):
    diff = sortNumbers[i][1] - i
    if result < diff:
        result = diff

print(result + 1)