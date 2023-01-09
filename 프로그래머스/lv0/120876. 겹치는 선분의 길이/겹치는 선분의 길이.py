def solution(lines):
    dic = {}
    for line in lines:
        for i in range(line[0], line[1]):
            if i not in dic:
                dic[i] = 0
            else:
                dic[i] += 1
    answer = 0
    dic = sorted(dic.items(), key= lambda x : x[0])
    for i in dic:
        if i[1]:
            answer += 1
    return answer