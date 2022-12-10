def solution(a, b):
    answer = 0
    while a:
        answer += a.pop()*b.pop()
    return answer