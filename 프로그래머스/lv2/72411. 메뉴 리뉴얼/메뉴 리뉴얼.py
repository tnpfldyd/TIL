import itertools
def solution(date, course):
    dic = {}
    for data in date:
        qw = set()
        for i in range(2, len(data)+1):
            for j in itertools.combinations(data, i):
                qw.add(j)
        for i in qw:
            i = ''.join(i)
            i = sorted(i)
            if ''.join(i) not in dic:
                dic[''.join(i)] = 1
            else:
                dic[''.join(i)] += 1
    answer = []
    for i in course:
        result = []
        max_v = 0
        for k, v in dic.items():
            if len(k) == i:
                result.append((k, v))
        for k, v in result:
            if v > max_v:
                max_v = v
        for k, v in result:
            if v == max_v and v > 1:
                answer.append(k)
    answer.sort()
    return answer