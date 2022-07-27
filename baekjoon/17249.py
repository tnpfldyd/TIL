text_ = input()
cnt = 0
lcnt = 0
for i in range(len(text_)):
    if text_[i] == '@':
        cnt += 1
    if text_[i] == '(':
        lcnt = cnt
        cnt = 0
print(lcnt, cnt)