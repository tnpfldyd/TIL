def solution(s):
    temp = {}
    result = []
    for idx, alpha in enumerate(s):
        if alpha not in temp:
            temp[alpha] = idx
            result.append(-1)
        else:
            result.append(idx-temp[alpha])
            temp[alpha] = idx
    return result