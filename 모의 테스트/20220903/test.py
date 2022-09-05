from audioop import reverse
import itertools, bisect
info = ["java backend junior pizza 150","python frontend senior chicken 210",
"python frontend senior chicken 150","cpp backend senior pizza 260",
"java backend junior chicken 80","python backend senior chicken 50"]
info2 = []
for i in info:
    temp = i.split()
    temp[-1] = int(temp[-1])
    info2.append(temp)
new_info = dict()
arr = [0,1,2,3]
for x in info2:
    qas = set()
    score = x[-1]
    qas.add(''.join(x[:-1]))
    for i in range(1, 5):
        for j in itertools.combinations(arr, i):
            temp = x[:-1]
            for idx in j:
                temp[idx] = '-'
            key = ''.join(temp)
            qas.add(key)
    for asdf in qas:
        if asdf not in new_info:
            new_info[asdf] = [score]
        else:
            new_info[asdf].append(score)
answer = []
for k, v in new_info.items():
    v.sort()
print(new_info)
query = ["java and backend and junior and pizza 100",
"python and frontend and senior and chicken 200",
"cpp and - and senior and pizza 250",
"- and backend and senior and - 150",
"- and - and - and chicken 100","- and - and - and - 150"]
for i in query:
    qw = i.split(' and ')
    qw[-1], scope = qw[-1].split()
    qw = ''.join(qw)
    scope = int(scope)
    cnt = 0
    if qw in new_info:
        cnt = len(new_info[qw]) - bisect.bisect_left(new_info[qw], scope)
    answer.append(cnt)
print(answer)