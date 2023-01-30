def solution(record):
    result = {}
    for i in record:
        i = i.split()
        if i[0] == 'Enter' or i[0] == 'Change':
            result[i[1]] = i[2]
    answer = []
    for i in record:
        i = i.split()
        if i[0] == 'Enter':
            answer.append(result[i[1]]+"님이 들어왔습니다.")
        elif i[0] == 'Leave':
            answer.append(result[i[1]]+"님이 나갔습니다.")
    return answer