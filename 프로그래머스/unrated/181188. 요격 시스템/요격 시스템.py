def solution(targets):
    answer = 0
    targets = sorted(targets, key=lambda x : x[1])
    end = 0
    for target in targets:
        s, e = target
        if s >= end:
            answer += 1
            end = e
    return answer