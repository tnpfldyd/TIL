def solution(today, terms, privacies):
    ty, tm, td = map(int, today.split('.'))
    grade_dic = {}
    for i in terms:
        grade, month = i.split()
        grade_dic[grade] = int(month)

    answer = []
    cnt = 1
    for priva in privacies:
        day, grade = priva.split()
        y, m, d = map(int, day.split('.'))
        m += grade_dic[grade]
        while m > 12:
            y += 1
            m -= 12
        if y < ty:
            answer.append(cnt)
        elif y == ty:
            if m < tm:
                answer.append(cnt)
            elif m == tm:
                if d <= td:
                    answer.append(cnt)
        cnt += 1
    return answer