def solution(arr):
    answer = []
    for i in arr:
        if len(answer) > 0:
            if answer[-1] != i:
                answer.append(i)
        else:
            answer.append(i)            
    return answer