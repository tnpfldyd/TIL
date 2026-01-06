N, M = map(int, input().split())
A = list(map(int, input().split()))
left, right = 0, 0
current_sum = 0
max_sum = 0
while right < N:
    current_sum += A[right]
    while current_sum > M:
        current_sum -= A[left]
        left += 1
    max_sum = max(max_sum, current_sum)
    right += 1
print(max_sum)