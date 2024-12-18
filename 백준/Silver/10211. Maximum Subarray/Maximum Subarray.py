import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    max_sum = -999_000
    current_sum = 0

    for value in arr:
        current_sum = max(value, current_sum + value)
        max_sum = max(max_sum, current_sum)

    print(max_sum)