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
    answer.append(7 - (cnt + zero) if cnt + zero > 0 else 6)
    answer.append(7 - cnt if cnt > 0 else 6)
    return answer