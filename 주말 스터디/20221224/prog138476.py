k = 6
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
orange_dic = {}
for i in tangerine:
    if i not in orange_dic:
        orange_dic[i] = 1
    else:
        orange_dic[i] += 1
print(orange_dic)
orange_dic = sorted(orange_dic.items(), key = lambda x : x[1])
print(orange_dic)
cnt = 0
while k > 0:
    k -= orange_dic.pop()[1]
    cnt += 1
print(cnt)