def solution(s):
    l, r = 0, 0
    strings = s.lower()
    for string in strings:
        if string == 'p':
            l += 1
        elif string == 'y':
            r += 1
    return l == r