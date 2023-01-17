def solution(rsp):
    rsp_dic = {'2':'0', '0':'5', '5':'2'}
    answer = ''
    for rs in rsp:
        answer += rsp_dic[rs]
    return answer