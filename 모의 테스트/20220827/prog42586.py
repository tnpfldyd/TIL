progresses = [93, 30, 55]
speeds = [1, 30, 5]
result = []
cnt = 0
while progresses:
    if progresses[0] >= 100:
        cnt += 1
        progresses.pop(0)
        speeds.pop(0)
    else:
        result.append(cnt)
        cnt = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
else:
    result.append(cnt)
rere = []
for j in result:
    if j != 0:
        rere.append(j)
print(rere)