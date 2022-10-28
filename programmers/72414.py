play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
result = "01:30:59"

def trans(time):
    h, m, s = map(int, time.split(':'))
    res = h * 3600 + m * 60 + s
    return res
visited = [0] * (trans(play_time)+1)

for log in logs:
    log1, log2 = log.split('-')
    visited[trans(log1)] += 1
    visited[trans(log2)] -= -1

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
print(answer)