today = "2020.01.01"
terms = ["Z 3", "D 5", "A 60"]
privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z", "2018.12.01 A"]
result = []
today = today.split('.')
for i in range(3):
    today[i] = int(today[i])
cnt = 1
term = {}
for i in terms:
    i = i.split()
    term[i[0]] = int(i[1])
for i in privacies:
    i = i.split()
    i[0] = i[0].split('.')
    for j in range(3):
        i[0][j] = int(i[0][j])
    temp = term[i[1]]
    i[0][1] += temp
    i[0][2] -= 1
    if i[0][2] == 0:
        i[0][2] = 28
        i[0][1] -= 1
    while i[0][1] > 12:
        i[0][0] += 1
        i[0][1] -= 12
    if today[0] > i[0][0]:
        result.append(cnt)
    else:
        if today[0] == i[0][0]:
            if today[1] > i[0][1]:
                result.append(cnt)
            else:
                if today[1] == i[0][1]:
                    if today[2] > i[0][2]:
                        result.append(cnt)
    cnt += 1
print(result)