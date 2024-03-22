import sys
from bisect import bisect_left
input = sys.stdin.readline

T = int(input())

for i in range(1, T + 1):
    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))
    arr = []
    arr.append(numbers[0])
    for k in range(1, N):
        cur = numbers[k]
        if arr[-1] < cur:
            arr.append(cur)
        else:
            k = bisect_left(arr, cur)
            arr[k] = cur

    print(f'Case #{i}')
    print(1 if len(arr) >= K else 0)