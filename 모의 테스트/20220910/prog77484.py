lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
cnt = 0
zero = 0
for i in lottos:
    if i != 0:
        if i in win_nums:
            cnt += 1
    else:
        zero += 1
answer = []
answer.append(7 - (cnt + zero) if cnt + zero > 0 else 6)
answer.append(7 - cnt if cnt > 0 else 6)
print(answer)