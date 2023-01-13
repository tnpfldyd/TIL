def solution(x):
    temp = sum(list(map(int, str(x))))
    if x % temp:
        answer = False
    else:
        answer = True
    return answer

print(solution(10))