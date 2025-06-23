import sys
input = sys.stdin.readline

def dfs(depth):
    if depth == M:
        print(*seq)
        return
    prev = 0
    for i in range(N):
        if not used[i] and numbers[i] != prev:
            used[i] = True
            seq.append(numbers[i])
            dfs(depth + 1)
            seq.pop()
            used[i] = False
            prev = numbers[i]

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
used = [False] * N
seq = []

dfs(0)