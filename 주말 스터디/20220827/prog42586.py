progresses = [93, 30, 55]
speeds = [1, 30, 5]
result = []
cnt = 0
while len(progresses) > 0:
    if progresses[0] >= 100:
        progresses.pop(0)
        speeds.pop(0)
        cnt += 1
    else:
        result.append(cnt)
        cnt = 0
        for i in range(len(progresses)):
            progresses[i] = progresses[i] + speeds[i]
result.append(cnt)
qw = []
for i in range(len(result)):
    if result[i] != 0:
        qw.append(result[i])
print(qw)