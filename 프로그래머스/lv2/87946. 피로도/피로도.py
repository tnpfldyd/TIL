import itertools
def solution(k, dungeons):
    num = [i for i in range(len(dungeons))]
    answer = 0
    for i in itertools.permutations(num, len(dungeons)):
        cnt = 0
        temp = k
        for j in i:
            if temp >= dungeons[j][0]:
                temp -= dungeons[j][1]
                cnt += 1
        if cnt > answer:
            answer = cnt
            if answer == len(dungeons):
                break
    return answer