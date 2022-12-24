def solution(k, tangerine):
    orange_dic = {}
    for i in tangerine:
        if i not in orange_dic:
            orange_dic[i] = 1
        else:
            orange_dic[i] += 1
    orange_dic = sorted(orange_dic.items(), key = lambda x : x[1])
    cnt = 0
    while k > 0:
        k -= orange_dic.pop()[1]
        cnt += 1
    return cnt