T = int(input())
for i in range(1, T+1):
    alpha_dic = {}
    string = input()
    for st in string:
        if st not in alpha_dic:
            alpha_dic[st] = 1
        else:
            alpha_dic[st] += 1
    cnt = 0
    for k, v in alpha_dic.items():
        if v == 2:
            cnt += 1
    answer = 'No'
    if cnt == 2:
        answer = 'Yes'
    print(f'#{i} {answer}')