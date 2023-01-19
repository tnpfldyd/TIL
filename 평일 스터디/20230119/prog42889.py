def solution(N, stages):
    result = {}
    for i in range(1, N+1):
        cnt = 0
        stage_pass = 0
        for j in stages:
            if j >= i:
                stage_pass += 1
            if j == i:
                cnt += 1
        if stage_pass == 0:
            temp = 0
        else:
            temp = cnt/stage_pass
        result[i] = temp
    result = sorted(result.items(), key = lambda x : -x[1])
    answer = []
    for k,v in result:
        answer.append(k)
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))