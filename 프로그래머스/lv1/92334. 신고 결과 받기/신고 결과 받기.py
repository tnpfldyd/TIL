def solution(id_list, report, k):
    qw = set(report)
    q = []
    for i in qw:
        q.append(i.split())
    result = [0]*len(id_list)
    for qwqw in q:
        temp = id_list.index(qwqw[1])
        result[temp] += 1
    rere = []
    for i in range(len(id_list)):
        if result[i] >= k:
            rere.append(id_list[i])
    reqw = [0]*len(id_list)
    for i in q:
        if i[1] in rere:
            temp = id_list.index(i[0])
            reqw[temp] += 1
    return reqw 