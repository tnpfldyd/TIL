import sys
input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    s, p = input().split()
    p = int(p)
    arr.append((s, p))

answer = 1e9

for _, p in arr:
    temp = 0
    for i in range(N):
        a, b = arr[i]
        if a == 'G':
            if p < b:
                temp += 1
        else:
            if p > b:
                temp += 1
    answer = min(answer, temp)

print(answer)