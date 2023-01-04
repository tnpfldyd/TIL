def solution(a, b):
    answer = ((abs(a - b) + 1) * (a + b)) // 2
    return answer

print(solution(3, 3))