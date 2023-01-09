def solution(my_string):
    number = []
    temp = ''
    operator = []
    for i in my_string:
        if i == ' ':
            continue
        elif i == '+' or i == '-':
            operator.append(i)
            number.append(int(temp))
            temp = ''
        else:
            temp += i
    number.append(int(temp))
    answer = number[0]
    for idx, oper in enumerate(operator, 1):
        if oper == '-':
            answer -= number[idx]
        else:
            answer += number[idx]
    return answer