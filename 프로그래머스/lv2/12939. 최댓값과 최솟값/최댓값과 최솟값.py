def solution(s):
    s = s.split()
    answer = ''
    max_ = -99999999
    min_ = 99999999
    for i in s:
        if int(i) > max_:
            max_ = int(i)
        if int(i) < min_:
            min_ = int(i)
    answer = f'{min_} {max_}'
    return answer