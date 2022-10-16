import itertools
k = 80
dungeons = [[80,20],[50,40],[30,10]]
num = [i for i in range(len(dungeons))]
answer = 0
for i in itertools.permutations(num, len(dungeons)):
    cnt = 0
    temp = k
    for j in i:
        if temp >= dungeons[j][0]:
            temp -= dungeons[j][1]
            cnt += 1
        else:
            break
    if cnt > answer:
        answer = cnt
print(answer)