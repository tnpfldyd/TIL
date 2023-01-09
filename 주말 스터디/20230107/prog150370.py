today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
result = [1, 3]

ty, tm, td = map(int, today.split('.'))
terms_dic = {}
answer = []
for i in terms:
    a, b = i.split(' ')
    terms_dic[a] = int(b)
cnt = 1
for i in privacies:
    day, grade = i.split(' ')
    y, m, d = map(int, day.split('.'))
    temp = terms_dic[grade]
    m += temp
    while m > 12:
        m -= 12
        y += 1
    if y < ty:
        answer.append(cnt)
    elif y == ty:
        if m < tm:
            answer.append(cnt)
        elif m == tm:
            if d <= td:
                answer.append(cnt)
    cnt += 1
print(answer)