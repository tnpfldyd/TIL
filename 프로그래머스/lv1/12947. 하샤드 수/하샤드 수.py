def solution(x):
    temp = str(x)
    temp = sum(list(map(int, temp)))
    if x % temp:
        answer = False
    else:
        answer = True
    return answer