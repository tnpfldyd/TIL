def solution(sequence, k):
    left = right = 0
    current_sum = 0
    min_s = min_e = 0
    min_length = float('inf')
    while right < len(sequence):
        current_sum += sequence[right]
        while current_sum > k:
            current_sum -= sequence[left]
            left += 1
        if current_sum == k:
            length = right - left + 1
            if length < min_length:
                min_length = length
                min_s, min_e = left, right
        right += 1
    return [min_s, min_e]