s = 'baabaa'
answer = []
for i in s:
    if len(answer) > 0:
        if answer[-1] == i:
            answer.pop()
        else:
            answer.append(i)
    else:
        answer.append(i)
print(answer)