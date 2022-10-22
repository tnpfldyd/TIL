def solution(new_id):
    answer = new_id
    answer = answer.lower()
    answer1 = ''
    for i in answer:
        if i in '1234567890-_.qwertyuiopasdfghjklzxcvbnm':
            answer1 += i
    answer2 = ''
    for i in answer1:
        if answer2 == '':
            answer2 += i
        else:
            if answer2[-1] == '.':
                if i != '.':
                    answer2 += i
            else:
                answer2 += i        
    if answer2[0] == '.':
        answer2 = answer2[1:]
    if answer2 != '':
        if answer2[-1] == '.':
            answer2 = answer2[:-1]
    if answer2 == '':
        answer2 = 'a'
    if len(answer2) > 15:
        answer2 = answer2[:15]
        if answer2[-1] == '.':
            answer2 = answer2[:-1]
    if len(answer2) <= 2:
        while len(answer2) != 3:
            answer2 += answer2[-1]
    return answer2