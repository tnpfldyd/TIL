def solution(s):
    answer = 0
    str_dic = {}
    check = ''
    for i in s:
        if not str_dic:
            str_dic[i] = 1
            check = i
        else:
            if i == check:
                str_dic[i] += 1
            else:
                if not str_dic.get('other'):
                    str_dic['other'] = 1
                else:
                    str_dic['other'] += 1
        if len(str_dic) == 2 and str_dic[check] == str_dic['other']:
            answer += 1
            str_dic = {}
    if str_dic:
        answer += 1
    return answer

print(solution('aaabbaccccabba'))