import sys
input = sys.stdin.readline

n = int(input().strip())
arr = [0] * (n + 1)
arr[0], arr[1] = 1, 1

for i in range(2, n + 1):
    arr[i] = (arr[i - 1] + arr[i - 2]) % 10

print(arr[n])