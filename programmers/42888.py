record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
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
        answer.append(result[i[1]]+'님이 나갔습니다.')
print(answer)