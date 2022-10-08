def solution(s):
    answer = []
    for i in s:
        if len(answer) > 0:
            if answer[-1] == i:
                answer.pop()
            else:
                answer.append(i)
        else:
            answer.append(i)
    if len(answer) > 0:
        return 0
    else:
        return 1