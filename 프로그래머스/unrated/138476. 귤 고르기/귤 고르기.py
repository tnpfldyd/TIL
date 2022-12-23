def solution(k, tangerine):
    apple_dic = {}
    for i in tangerine:
        if i not in apple_dic:
            apple_dic[i] = 1
        else:
            apple_dic[i] += 1
    apple_dic = sorted(apple_dic.items(), key=lambda x : -x[1])
    cnt = 0
    for i, cost in apple_dic:
        if k < 1:
            break
        k -= cost
        cnt += 1
    return cnt