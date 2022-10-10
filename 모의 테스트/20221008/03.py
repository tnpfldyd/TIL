s = "3people unFollowed me"
s = s.lower()
answer = ''
cnt = 0
for i in s:
    if cnt == 0 and i not in '0123456789':
        answer += i.upper()
    else:
        answer += i
    cnt += 1
    if i == ' ':
        cnt = 0
print(answer)