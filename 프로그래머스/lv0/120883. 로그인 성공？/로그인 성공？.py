def solution(id_pw, db):
    answer = ''
    db_dic = {}
    for a, b in db:
        db_dic[a] = b
    if id_pw[0] not in db_dic:
        answer = 'fail'
    else:
        if db_dic[id_pw[0]] != id_pw[1]:
            answer = 'wrong pw'
        else:
            answer = 'login'
    return answer