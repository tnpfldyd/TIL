import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
ops = list(map(int, input().split()))

MAX = -10**18
MIN = 10**18

def div(a, b):
    if a < 0:
        return -(-a // b)
    return a // b

def dfs(idx, value):
    global MAX, MIN

    if idx == N:
        MAX = max(MAX, value)
        MIN = min(MIN, value)
        return

    for i in range(4):
        if ops[i] > 0:
            ops[i] -= 1

            if i == 0:
                dfs(idx + 1, value + A[idx])
            elif i == 1:
                dfs(idx + 1, value - A[idx])
            elif i == 2:
                dfs(idx + 1, value * A[idx])
            else:
                dfs(idx + 1, div(value, A[idx]))

            ops[i] += 1

dfs(1, A[0])

print(MAX)
print(MIN)