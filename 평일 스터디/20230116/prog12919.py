
def solution(seoul):
    idx = 0
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            idx = i
            break
    answer = '김서방은 ' + str(idx) + '에 있다'
    return answer

print(solution(["Jane", "Kim"]))
