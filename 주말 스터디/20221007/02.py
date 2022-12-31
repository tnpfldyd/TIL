import itertools
stats = [2,5,6,7,8,4]
count = 0
for i in range(len(stats)):
    temp = []
    cnt = 0
    count = 0
    for j in range(len(stats)):
        if i == j:
            continue
        temp.append(stats[j])
    for j in temp:
        if count == 0:
            cnt += j
            count += 1
        else:
            cnt -= j
            count -= 1
    if cnt == 0:
        print(i+1)
        break
else:
    print(-1)
