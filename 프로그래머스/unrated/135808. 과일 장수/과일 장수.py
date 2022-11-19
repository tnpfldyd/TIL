def solution(k, m, score):
    score.sort(reverse=True)
    cnt = 0
    result = 0
    for i in score:
        cnt += 1
        if cnt == m:
            result += m*i
            cnt = 0
    return result