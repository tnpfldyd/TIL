N, K = map(int, input().split())

def binarySearch(left, right):
    while left <= right:
        mid = (left + right) // 2
        temp = (mid + 1) * ((N - mid) + 1)
        if temp > K:
            right = mid - 1
        elif temp < K:
            left = mid + 1
        else:
            return 'YES'
    return 'NO'
answer = binarySearch(0, N // 2)
print(answer)