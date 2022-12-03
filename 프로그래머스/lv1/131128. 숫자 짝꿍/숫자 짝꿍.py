def solution(X, Y):
    x_cnt = {}
    y_cnt = {}
    result = ''
    flag = False
    for i in X:
        if i not in x_cnt:
            x_cnt[i] = 1
        else:
            x_cnt[i] += 1
    for i in Y:
        if i not in y_cnt:
            y_cnt[i] = 1
        else:
            y_cnt[i] += 1
    for i in x_cnt:
        if y_cnt.get(i):
            cnt = min(x_cnt[i], y_cnt[i])
            result += i*cnt
            if i != '0':
                flag = True
    if not flag and result:
        return '0'
    elif not result:
        return '-1'
    else:
        result = sorted(result, reverse=True)
        result = ''.join(result)
        return result
