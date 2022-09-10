def solution(lottos, win_nums):
    cnt = 0
    zero = 0
    for i in lottos:
        if i != 0:
            if i in win_nums:
                cnt += 1
        else:
            zero += 1
    answer = []
    if cnt + zero > 0:
        answer.append(7 - (cnt + zero))
    else:
        answer.append(6)
    if cnt > 0:
        answer.append(7 - cnt)
    else:
        answer.append(6)
    return answer