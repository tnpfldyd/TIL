def trans(time):
    h, m, s = map(int, time.split(':'))
    res = h * 3600 + m * 60 + s
    return res
def solution(play_time, adv_time, logs):
    visited = [0] * (trans(play_time)+1)

    for log in logs:
        log1, log2 = log.split('-')
        visited[trans(log1)] += 1
        visited[trans(log2)] -= 1

    for i in range(1, len(visited)):
        visited[i] += visited[i-1]

    temp = sum(visited[:trans(adv_time)])
    max_num = temp
    idx = 0
    for i in range(trans(adv_time), len(visited)-1):
        temp += visited[i] - visited[i-trans(adv_time)]
        if temp > max_num:
            max_num = temp
            idx = i-trans(adv_time)+1
    s = str(idx%60)
    m = str((idx//60) % 60)
    h = str(idx//3600)
    answer = ''
    for i in (h,m,s):
        while len(i) < 2:
            i = '0'+i
        if not len(answer):
            answer += i
        else:
            answer += ':'+i
    return answer