import sys
input = sys.stdin.readline

N = int(input())
numbers = [(int(input()), i) for i in range(N)]
sortNumbers = sorted(numbers)
result = max(sortNumbers[i][1] - i for i in range(N)) + 1
print(result)