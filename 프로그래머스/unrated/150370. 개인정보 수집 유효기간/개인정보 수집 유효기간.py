def solution(today, terms, privacies):
    ty,tm,td = map(int, today.split('.'))
    terms_dic = {}
    for term in terms:
        grade, month = term.split()
        terms_dic[grade] = int(month)
    answer = []
    cnt = 1
    for privacy in privacies:
        day, grade = privacy.split()
        y, m, d = map(int, day.split('.'))
        m += terms_dic[grade]
        while m > 12:
            m -= 12
            y += 1
        if ty > y:
            answer.append(cnt)
        elif ty == y:
            if tm > m:
                answer.append(cnt)
            elif tm == m:
                if td >= d:
                    answer.append(cnt)
        cnt += 1
    return answer
