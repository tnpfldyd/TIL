import sys

sys.setrecursionlimit(10000)

N = int(input())
numbers = list(map(int, input().split()))
plus, minus, multiply, divide = map(int, input().split())

max_result = -int(1e9)
min_result = int(1e9)

def dfs(index, current_result, p, m, mul, d):
    global max_result, min_result

    if index == N:
        max_result = max(max_result, current_result)
        min_result = min(min_result, current_result)
        return

    num = numbers[index]

    if p > 0:
        dfs(index + 1, current_result + num, p - 1, m, mul, d)
    if m > 0:
        dfs(index + 1, current_result - num, p, m - 1, mul, d)
    if mul > 0:
        dfs(index + 1, current_result * num, p, m, mul - 1, d)
    if d > 0:
        if current_result < 0:
            dfs(index + 1, -(-current_result // num), p, m, mul, d - 1)
        else:
            dfs(index + 1, current_result // num, p, m, mul, d - 1)

dfs(1, numbers[0], plus, minus, multiply, divide)

print(max_result)
print(min_result)