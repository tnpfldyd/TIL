import sys
input = sys.stdin.readline

N = int(input())
arr = sorted([int(input()) for _ in range(N)])
sums = []
for i in range(N):
    for j in range(i, N):
        sums.append(arr[i] +  arr[j])

sums.sort()
result = 0
for i in range(N):
    for j in range(i, N):
        temp = arr[j] - arr[i]
        left, right = 0, len(sums) - 1
        while left <= right:
            mid = (left + right)  // 2
            cur = sums[mid]
            if temp > cur:
                left = mid + 1
            elif temp < cur:
                right = mid - 1
            else:
                result = max(result, arr[j])
                break
print(result)