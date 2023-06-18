def is_possible(mid_value):
    total_sum = 0
    group_count = 1
    for i in range(N):
        total_sum += arr[i]
        if total_sum > mid_value:
            total_sum = arr[i]
            group_count += 1
    return group_count <= M


def print_ans(mid_value):
    print(mid_value)
    global M
    i = 0
    current_sum = 0
    marble_count = 0
    while i < N:
        current_sum += arr[i]
        if current_sum > mid_value:
            current_sum = arr[i]
            M -= 1
            print(marble_count, end=" ")
            marble_count = 0
        marble_count += 1
        if N - i == M:
            break
        i += 1

    while M:
        print(marble_count, end=" ")
        marble_count = 1
        M -= 1


N, M = map(int, input().split())
arr = list(map(int, input().split()))

left = max(arr)
right = sum(arr)
mid_value = 0

while left <= right:
    mid_value = (left + right) // 2
    if is_possible(mid_value):
        right = mid_value - 1
    else:
        left = mid_value + 1

print_ans(left)