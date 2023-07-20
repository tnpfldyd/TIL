import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())

arr = [0] * N
result = 0

def check(x):
    for i in range(x):
        if arr[i] == arr[x] or abs(arr[x] - arr[i]) == x - i:
            return False
    return True

def dfs(x):
    if x == N:
        global result
        result += 1
        return
    for i in range(N):
        arr[x] = i
        if check(x):
            dfs(x + 1)

dfs(0)
print(result)