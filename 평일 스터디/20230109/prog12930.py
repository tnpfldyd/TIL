s = "try hello world"
s = s.split(' ')
answer = ''
for i in s:
    temp = ''
    for j in range(len(i)):
        if not j % 2:
            temp += i[j].upper()
        else:
            temp += i[j].lower()
    temp += ' '
    answer += temp
print(answer[:-1])