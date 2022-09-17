def solution(dartResult):
    result = []
    temp = 0
    num = ['0','1','2','3','4','5','6','7','8','9']
    for i in range(len(dartResult)):
        if dartResult[i] == '0' and temp == 10:
            continue
        if dartResult[i] == '1' and dartResult[i+1] == '0':
            temp = 10
        elif dartResult[i] in num:
            temp = int(dartResult[i])
        elif dartResult[i] == 'S':
            result.append(temp**1)
            temp = 0
        elif dartResult[i] == 'D':
            result.append(temp**2)
            temp = 0
        elif dartResult[i] == 'T':
            result.append(temp**3)
            temp = 0
        elif dartResult[i] == '*':
            if len(result) > 1:
                result[-1] *= 2
                result[-2] *= 2
            else:
                result[-1] *= 2
        elif dartResult[i] == '#':
            result[-1] = -result[-1]
    return sum(result)