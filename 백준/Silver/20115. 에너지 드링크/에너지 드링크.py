import sys
input = sys.stdin.readline

N = int(input())
drinks = list(map(float, input().split()))

drinks.sort()

result = drinks[-1]
for i in range(N - 1):
    result += drinks[i] / 2

print(result)