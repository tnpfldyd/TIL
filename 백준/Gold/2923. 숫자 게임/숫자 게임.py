import sys
input = sys.stdin.readline

def get_min_max_sum():
    original_a = [a[i] for i in range(101)]
    original_b = [b[i] for i in range(101)]

    idx_a, idx_b = get_non_zero_index(a, 1, False), get_non_zero_index(b, 100, True)
    min_value = min(a[idx_a], b[idx_b])
    a[idx_a] -= min_value
    b[idx_b] -= min_value

    max_sum = 0
    while idx_a != -1 and idx_b != -1:
        max_sum = max(max_sum, idx_a + idx_b)

        idx_a, idx_b = get_non_zero_index(a, idx_a, False), get_non_zero_index(b, idx_b, True)
        min_value = min(a[idx_a], b[idx_b])
        a[idx_a] -= min_value
        b[idx_b] -= min_value

    for i in range(1, 101):
        a[i] = original_a[i]
        b[i] = original_b[i]

    return max_sum

def get_non_zero_index(nums, start_index, is_reversed):
    if not is_reversed:
        for i in range(start_index, 101):
            if nums[i] >= 1:
                return i
    else:
        for i in range(start_index, 0, -1):
            if nums[i] >= 1:
                return i

    return -1

if __name__ == '__main__':
    N = int(input())

    a = [0]*101
    b = [0]*101

    for _ in range(N):
        ai, bi = map(int, input().split())
        a[ai] += 1
        b[bi] += 1

        min_max_sum = get_min_max_sum()
        print(min_max_sum)