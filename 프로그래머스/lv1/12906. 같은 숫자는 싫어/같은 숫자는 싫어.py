def solution(arr):
    answer = []
    for i in arr:
        if answer:
            if answer[-1] != i:
                answer.append(i)
        else:
            answer.append(i)
    return answer