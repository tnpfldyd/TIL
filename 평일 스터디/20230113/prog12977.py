import itertools

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if not x % i:
            return False
    return True

def solution(nums):
    answer = 0
    for i in itertools.combinations(nums, 3):
        if is_prime(sum(i)):
            answer += 1
    return answer

print(solution([3,3,3,3]))
