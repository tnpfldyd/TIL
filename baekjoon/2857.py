tong = {}
cnt = 0
for i in range(1, 6):
    name = (input())
    if name.count('FBI') > 0:
        tong[name] = i
        cnt += 1
    else:
        tong[name] = 0
result = [v for k, v in tong.items() if v > 0]

if cnt == 0:
    print('HE GOT AWAY!')
else:
    print(*result)