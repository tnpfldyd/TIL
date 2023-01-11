def solution(quiz):
    answer = []
    for string in quiz:
        string = string.split()
        if string[1] == '-':
            if int(string[0]) - int(string[2]) == int(string[4]):
                answer.append('O')
            else:
                answer.append('X')
        else:
            if int(string[0]) + int(string[2]) == int(string[4]):
                answer.append('O')
            else:
                answer.append('X')
    return answer

print(solution(["3 - 4 = -3", "5 + 6 = 11"]))