N, C = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

def solve(N, C, numbers):
    left, right = 0, N - 1
    while left < right:
        left_number, right_number = numbers[left], numbers[right]
        if left_number == C or right_number == C:
            return 1
        elif left_number + right_number == C:
            return 1
        
        for i in range(N):
            if left == i or right == i:
                continue
            if numbers[i] + left_number + right_number == C:
                return 1
        
        if left_number + right_number < C:
            left += 1
        else:
            right -= 1
    return 0

answer = solve(N, C, numbers)
print(answer)