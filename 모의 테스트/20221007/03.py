adventures = "dccccd"
k = 3
answer = 0
for i in range(len(adventures)-k+1):
    temp = {}
    cnt = 0
    for j in range(i, k+i):
        if adventures[j] in temp:
            temp[adventures[j]] += 1
        else:
            temp[adventures[j]] = 1
    for e, v in temp.items():
        cnt += ((ord(e)-96) ** v)
    cnt = cnt % (10**9 + 7)
    if answer < cnt:
        answer = cnt
